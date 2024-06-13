using Microsoft.Data.SqlClient;
using System;
using System.Data;
using System.Windows.Forms;

namespace Practic
{
    public partial class Form1 : Form
    {
        string connectionString = @"Server=MARIA\SQLEXPRESS;Database=S13;Integrated Security=true;TrustServerCertificate=true;";
        DataSet ds = new DataSet();
        SqlDataAdapter parentAdapter;
        SqlDataAdapter childAdapter;
        BindingSource bsParent;
        BindingSource bsChild;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                using (SqlConnection conn = new SqlConnection(connectionString))
                {
                    conn.Open();
                    parentAdapter = new SqlDataAdapter("SELECT * FROM Muzee", conn);
                    childAdapter = new SqlDataAdapter("SELECT * FROM Expozitii", conn);
                    parentAdapter.Fill(ds, "Muzee");
                    childAdapter.Fill(ds, "Expozitii");

                    bsParent = new BindingSource();
                    bsParent.DataSource = ds.Tables["Muzee"];
                    dataGridViewMuzee.DataSource = bsParent;

                    DataColumn parentColumn = ds.Tables["Muzee"].Columns["Mid"];
                    DataColumn childColumn = ds.Tables["Expozitii"].Columns["Mid"];
                    DataRelation relation = new DataRelation("fk_m_e", parentColumn, childColumn);
                    ds.Relations.Add(relation);

                    bsChild = new BindingSource();
                    bsChild.DataSource = bsParent;
                    bsChild.DataMember = "fk_m_e";
                    dataGridViewExpozitii.DataSource = bsChild;

                    textBoxDenumire.DataBindings.Add("Text", bsChild, "Denumire", true);
                    textBoxDescriere.DataBindings.Add("Text", bsChild, "Descriere", true);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (!string.IsNullOrEmpty(textBoxDenumire.Text) && !string.IsNullOrEmpty(textBoxDescriere.Text))
                {
                    using (SqlConnection conn = new SqlConnection(connectionString))
                    {
                        conn.Open();
                        childAdapter.InsertCommand = new SqlCommand("INSERT INTO Expozitii VALUES (@denumire, @descriere, @dataInceput, @dataSfarsit, @mid)", conn);
                        childAdapter.InsertCommand.Parameters.AddWithValue("@denumire", textBoxDenumire.Text);
                        childAdapter.InsertCommand.Parameters.AddWithValue("@descriere", textBoxDescriere.Text);
                        childAdapter.InsertCommand.Parameters.AddWithValue("@dataInceput", Convert.ToDateTime(dateTimePickerStart.Value));
                        childAdapter.InsertCommand.Parameters.AddWithValue("@dataSfarsit", Convert.ToDateTime(dateTimePickerEnd.Value));
                        childAdapter.InsertCommand.Parameters.AddWithValue("@mid", Convert.ToInt32(dataGridViewMuzee.CurrentRow.Cells["Mid"].Value));

                        // Execute the insert command
                        int rowsAffected = childAdapter.InsertCommand.ExecuteNonQuery();

                        parentAdapter.SelectCommand.Connection = conn;
                        childAdapter.SelectCommand.Connection = conn;
                        ds.Tables["Expozitii"].Clear();
                        ds.Tables["Muzee"].Clear();
                        parentAdapter.Fill(ds, "Muzee");
                        childAdapter.Fill(ds, "Expozitii");

                        conn.Close();

                        // If insertion is successful, notify the user
                        if (rowsAffected > 0)
                        {
                            MessageBox.Show("Insertion successful!");
                        }
                        else
                        {
                            MessageBox.Show("Insertion failed!");
                        }
                    }
                }
                else
                {
                    MessageBox.Show("Please fill in all fields before adding a record.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (!string.IsNullOrEmpty(textBoxDenumire.Text) && !string.IsNullOrEmpty(textBoxDescriere.Text))
                {
                    using (SqlConnection conn = new SqlConnection(connectionString))
                    {
                        conn.Open();

                        childAdapter.UpdateCommand = new SqlCommand("UPDATE Expozitii SET Denumire=@denumire, Descriere=@descriere, DataIncepere=@dataInceput, DataInchidere=@dataSfarsit WHERE Eid=@eid", conn);

                        // Add parameters to the SqlCommand
                        childAdapter.UpdateCommand.Parameters.Add("@denumire", SqlDbType.VarChar).Value = textBoxDenumire.Text;
                        childAdapter.UpdateCommand.Parameters.Add("@descriere", SqlDbType.VarChar).Value = textBoxDescriere.Text;
                        childAdapter.UpdateCommand.Parameters.Add("@dataInceput", SqlDbType.Date).Value = Convert.ToDateTime(dateTimePickerStart.Value);
                        childAdapter.UpdateCommand.Parameters.Add("@dataSfarsit", SqlDbType.Date).Value = Convert.ToDateTime(dateTimePickerEnd.Value);
                        childAdapter.UpdateCommand.Parameters.Add("@eid", SqlDbType.Int).Value = dataGridViewExpozitii.CurrentRow.Cells["Eid"].Value;

                        // Execute the insert command
                        int rowsAffected = childAdapter.UpdateCommand.ExecuteNonQuery();

                        parentAdapter.SelectCommand.Connection = conn;
                        childAdapter.SelectCommand.Connection = conn;
                        ds.Tables["Expozitii"].Clear();
                        ds.Tables["Muzee"].Clear();
                        parentAdapter.Fill(ds, "Muzee");
                        childAdapter.Fill(ds, "Expozitii");

                        conn.Close();

                        // If update is successful, notify the user
                        if (rowsAffected > 0)
                        {
                            MessageBox.Show("The record has been updated successfully!");
                        }
                        else
                        {
                            MessageBox.Show("Update failed!");
                        }
                    }
                }
                else
                {
                    MessageBox.Show("Please fill in all fields before adding a record.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void deleteButton_Click(object sender, EventArgs e)
        {
            try
            {
                using (SqlConnection conn = new SqlConnection(connectionString))
                {
                    conn.Open();

                    childAdapter.DeleteCommand = new SqlCommand("DELETE FROM Expozitii WHERE Eid=@eid", conn);

                    childAdapter.DeleteCommand.Parameters.Add("@eid", SqlDbType.Int).Value = dataGridViewExpozitii.CurrentRow.Cells["Eid"].Value;

                    // Execute the insert command
                    int rowsAffected = childAdapter.DeleteCommand.ExecuteNonQuery();

                    parentAdapter.SelectCommand.Connection = conn;
                    childAdapter.SelectCommand.Connection = conn;
                    ds.Tables["Expozitii"].Clear();
                    ds.Tables["Muzee"].Clear();
                    parentAdapter.Fill(ds, "Muzee");
                    childAdapter.Fill(ds, "Expozitii");

                    conn.Close();

                    // If delete is successful, notify the user
                    if (rowsAffected > 0)
                    {
                        MessageBox.Show("The record has been deleted successfully!");
                    }
                    else
                    {
                        MessageBox.Show("Delete failed!");
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }


        private void label3_Click(object sender, EventArgs e)
        {

        }
    }
}
