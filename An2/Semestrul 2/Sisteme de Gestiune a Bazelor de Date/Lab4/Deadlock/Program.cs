using System.Data.SqlClient;

namespace Deadlock
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string connectionString = @"Server=MARIA\SQLEXPRESS;Database=Calatorii;Integrated Security=true;TrustServerCertificate=true;";
            int retryCount = 0;
            bool success = false;

            while (retryCount < 5 && !success)
            {
                Console.WriteLine("Retry count: " + retryCount);

                Thread thread1 = new Thread(() => 
                { 
                    Console.WriteLine("Thread1 is running!");

                    using (SqlConnection con = new SqlConnection(connectionString))
                    {
                        con.Open();

                        // Create a new transaction
                        using (SqlTransaction transaction = con.BeginTransaction())
                        {
                            try
                            {
                                using (SqlCommand command = con.CreateCommand())
                                {
                                    command.Transaction = transaction;

                                    // update 1
                                    command.CommandText = "UPDATE Clienti SET Telefon = '0700000001' WHERE Nume = 'Popescu'";
                                    command.ExecuteNonQuery();

                                    // delay for 10 sec
                                    Thread.Sleep(10000);

                                    // update 2
                                    command.CommandText = "UPDATE PacheteTuristice SET Pret = '1.99' WHERE NumePachet = 'Vacanta la Paris'";
                                    command.ExecuteNonQuery();
                                }

                                // Commit the tran
                                transaction.Commit();
                                Console.WriteLine("Transaction committed successfully.");
                                success = true;
                            } catch (SqlException ex)
                            {
                                // Deadlock error number
                                if(ex.Number == 1205)
                                {
                                    Console.WriteLine("Deadlock occured. \nRetrying...");

                                    transaction.Rollback();
                                    Console.WriteLine("Transaction rolled back.");
                                    retryCount++;
                                }
                                // Handle other exceptions
                                else
                                {
                                    Console.WriteLine("Error occurred: " + ex.Message);
                                    transaction.Rollback();
                                    Console.WriteLine("Transaction rolled back.");
                                }
                            }
                        }
                    }
                });

                Thread thread2 = new Thread(() =>
                {
                    Console.WriteLine("Thread2 is running!");

                    using (SqlConnection con = new SqlConnection(connectionString))
                    {
                        con.Open();

                        // Set the deadlock priority to LOW
                        using (SqlCommand setDeadlockPriorityCmd = con.CreateCommand())
                        {
                            setDeadlockPriorityCmd.CommandText = "SET DEADLOCK_PRIORITY LOW";
                            setDeadlockPriorityCmd.ExecuteNonQuery();
                        }

                        // Create a new transaction
                        using (SqlTransaction transaction = con.BeginTransaction())
                        {
                            try
                            {
                                using (SqlCommand command = con.CreateCommand())
                                {
                                    command.Transaction = transaction;

                                    // update 1
                                    command.CommandText = "UPDATE PacheteTuristice SET Pret = '2.99' WHERE NumePachet = 'Vacanta la Paris'";
                                    command.ExecuteNonQuery();

                                    // delay for 10 sec
                                    Thread.Sleep(10000);

                                    //upsate 2
                                    command.CommandText = "UPDATE Clienti SET Telefon = '0700000002' WHERE Nume = 'Popescu';";
                                    command.ExecuteNonQuery();
                                }

                                // Commit the tran
                            } catch (SqlException ex)
                            {
                                // Deadlock error number
                                if (ex.Number == 1205)
                                {
                                    Console.WriteLine("Deadlock occured. \nRetrying...");

                                    transaction.Rollback();
                                    Console.WriteLine("Transaction rolled back.");
                                    retryCount++;
                                }
                                // Handle other exceptions
                                else
                                {
                                    Console.WriteLine("Error occurred: " + ex.Message);
                                    transaction.Rollback();
                                    Console.WriteLine("Transaction rolled back.");
                                }
                            }
                        }
                    }
                });

                thread1.Start();
                thread2.Start();
                thread1.Join();
                thread2.Join();
            }

            if (retryCount >= 5)
            {
                Console.WriteLine("Exceeded maximum retry attempts! Abording.");
            }
            else
            {
                Console.WriteLine("All transactions completed.");
            }
        }
    }
}
