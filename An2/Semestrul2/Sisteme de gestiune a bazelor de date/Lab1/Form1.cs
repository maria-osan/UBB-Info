using Microsoft.Data.SqlClient;
using System;
using System.Data;
using System.Windows.Forms;

namespace Lab1
{
    public partial class Form1 : Form
    {
        string connectionString = @"Server=MARIA\SQLEXPRESS;Database=Calatorii;Integrated Security=true;TrustServerCertificate=true;";
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
                using(SqlConnection conn = new SqlConnection(connectionString))
                {
                    conn.Open();
                    //MessageBox.Show("Starea conexiunii: " + conn.State.ToString());
                    parentAdapter = new SqlDataAdapter("SELECT * FROM Destinatii", conn);
                    childAdapter = new SqlDataAdapter("SELECT * FROM PacheteTuristice", conn);
                    parentAdapter.Fill(ds, "Destinatii");
                    childAdapter.Fill(ds, "PacheteTuristice");

                    bsParent = new BindingSource();
                    bsParent.DataSource = ds.Tables["Destinatii"];
                    dataGridParent.DataSource = bsParent;

                    DataColumn parentColumn = ds.Tables["Destinatii"].Columns["IDDestinatie"];
                    DataColumn childColumn = ds.Tables["PacheteTuristice"].Columns["DestinatieID"];
                    DataRelation relation = new DataRelation("FK_D_PT", parentColumn, childColumn);
                    ds.Relations.Add(relation);

                    bsChild = new BindingSource();
                    bsChild.DataSource = bsParent;
                    bsChild.DataMember = "FK_D_PT";
                    dataGridChild.DataSource = bsChild;

                    labelRecordsDestinatii.Text = "Record " + (bsParent.Position + 1) + " of " + bsParent.Count;
                    labelRecordsPacheteTuristice.Text = "Record " + (bsChild.Position + 1) + " of " + bsChild.Count;

                    textBoxNumePachet.DataBindings.Add("Text", bsChild, "NumePachet", true);
                    textBoxDescriere.DataBindings.Add("Text", bsChild, "Descriere", true);
                    textBoxPret.DataBindings.Add("Text", bsChild, "Pret", true);
                }
            }
            catch (Exception ex) 
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void buttonReload_Click(object sender, EventArgs e)
        {
            try
            {
                using (SqlConnection conn = new SqlConnection(connectionString))
                {
                    parentAdapter.SelectCommand.Connection = conn;
                    childAdapter.SelectCommand.Connection = conn;
                    ds.Tables["PacheteTuristice"].Clear();
                    ds.Tables["Destinatii"].Clear();
                    parentAdapter.Fill(ds, "Destinatii");
                    childAdapter.Fill(ds, "PacheteTuristice");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            try
            {
                if(!string.IsNullOrEmpty(textBoxNumePachet.Text) && !string.IsNullOrEmpty(textBoxDescriere.Text) && !string.IsNullOrEmpty(textBoxPret.Text))
                {
                    using (SqlConnection conn = new SqlConnection(connectionString))
                    {
                        conn.Open();

                        SqlCommand getMaxIdCommand = new SqlCommand("SELECT MAX(IDPachetTuristic) FROM PacheteTuristice", conn);
                        int maxId = Convert.ToInt32(getMaxIdCommand.ExecuteScalar());
                        int nextId = maxId + 1; // Increment the maximum ID to get the next available ID

                        int destinatieId = Convert.ToInt32(dataGridParent.CurrentRow.Cells["IDDestinatie"].Value);

                        childAdapter.InsertCommand = new SqlCommand("INSERT INTO PacheteTuristice (IDPachetTuristic, NumePachet, Descriere, Pret, DestinatieID) VALUES (@id, @nume, @descriere, @pret, @idDestinatie)", conn);
                        childAdapter.InsertCommand.Parameters.AddWithValue("@id", nextId);
                        childAdapter.InsertCommand.Parameters.AddWithValue("@nume", textBoxNumePachet.Text);
                        childAdapter.InsertCommand.Parameters.AddWithValue("@descriere", textBoxDescriere.Text);
                        childAdapter.InsertCommand.Parameters.AddWithValue("@pret", Convert.ToDecimal(textBoxPret.Text));
                        childAdapter.InsertCommand.Parameters.AddWithValue("@idDestinatie", destinatieId);

                        // Execute the insert command
                        int rowsAffected = childAdapter.InsertCommand.ExecuteNonQuery();

                        parentAdapter.SelectCommand.Connection = conn;
                        childAdapter.SelectCommand.Connection = conn;
                        ds.Tables["PacheteTuristice"].Clear();
                        ds.Tables["Destinatii"].Clear();
                        parentAdapter.Fill(ds, "Destinatii");
                        childAdapter.Fill(ds, "PacheteTuristice");

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

        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            try
            {
                if(!string.IsNullOrEmpty(textBoxNumePachet.Text) && !string.IsNullOrEmpty(textBoxDescriere.Text) && !string.IsNullOrEmpty(textBoxPret.Text))
                {
                    using (SqlConnection conn = new SqlConnection(connectionString))
                    {
                        conn.Open();

                        childAdapter.UpdateCommand = new SqlCommand("UPDATE PacheteTuristice SET NumePachet=@nume, Descriere=@descriere, Pret=@pret WHERE IDPachetTuristic=@id", conn);

                        // Add parameters to the SqlCommand
                        childAdapter.UpdateCommand.Parameters.Add("@nume", SqlDbType.VarChar).Value = textBoxNumePachet.Text;
                        childAdapter.UpdateCommand.Parameters.Add("@descriere", SqlDbType.VarChar).Value = textBoxDescriere.Text;
                        childAdapter.UpdateCommand.Parameters.Add("@pret", SqlDbType.Float).Value = Convert.ToDouble(textBoxPret.Text);
                        childAdapter.UpdateCommand.Parameters.Add("@id", SqlDbType.Int).Value = dataGridChild.CurrentRow.Cells["IDPachetTuristic"].Value;

                        // Execute the update command
                        int rowsAffected = childAdapter.UpdateCommand.ExecuteNonQuery();

                        parentAdapter.SelectCommand.Connection = conn;
                        childAdapter.SelectCommand.Connection = conn;
                        ds.Tables["PacheteTuristice"].Clear();
                        ds.Tables["Destinatii"].Clear();
                        parentAdapter.Fill(ds, "Destinatii");
                        childAdapter.Fill(ds, "PacheteTuristice");

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
                    MessageBox.Show("Please fill in all fields before updating the record.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void buttonDelete_Click(object sender, EventArgs e)
        {
            DialogResult dr;
            dr = MessageBox.Show("Are you sure?\nNo undo after delete", "Confirm Deletion", MessageBoxButtons.YesNo);
            if (dr == DialogResult.Yes)
            {
                try
                {
                    using (SqlConnection conn = new SqlConnection(connectionString))
                    {
                        conn.Open();

                        childAdapter.DeleteCommand = new SqlCommand("DELETE FROM PacheteTuristice WHERE IDPachetTuristic=@id", conn);

                        childAdapter.DeleteCommand.Parameters.Add("@id", SqlDbType.Int).Value = dataGridChild.CurrentRow.Cells["IDPachetTuristic"].Value;

                        // Execute the delete command
                        int rowsAffected = childAdapter.DeleteCommand.ExecuteNonQuery();

                        parentAdapter.SelectCommand.Connection = conn;
                        childAdapter.SelectCommand.Connection = conn;
                        ds.Tables["PacheteTuristice"].Clear();
                        ds.Tables["Destinatii"].Clear();
                        parentAdapter.Fill(ds, "Destinatii");
                        childAdapter.Fill(ds, "PacheteTuristice");

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
            else
            {
                MessageBox.Show("Deletion Aborded");
            }
        }

        private void dataGridParentUpdate()
        {
            dataGridParent.ClearSelection();
            dataGridParent.Rows[bsParent.Position].Selected = true;
            recordsDestinatii();
        }

        private void recordsDestinatii()
        {
            labelRecordsDestinatii.Text = "Record " + (bsParent.Position + 1)  + " of " + bsParent.Count;
        }

        private void buttonFirstDestinatie_Click(object sender, EventArgs e)
        {
            bsParent.MoveFirst();
            dataGridParentUpdate();
            recordsDestinatii();
        }

        private void buttonPreviousDestinatie_Click(object sender, EventArgs e)
        {
            bsParent.MovePrevious();
            dataGridParentUpdate();
            recordsDestinatii();
        }

        private void buttonNextDestinatie_Click(object sender, EventArgs e)
        {
            bsParent.MoveNext();
            dataGridParentUpdate();
            recordsDestinatii();
        }

        private void buttonLastDestinatie_Click(object sender, EventArgs e)
        {
            bsParent.MoveLast();
            dataGridParentUpdate();
            recordsDestinatii();
        }

        private void dataGridChildUpdate()
        {
            dataGridChild.ClearSelection();
            dataGridChild.Rows[bsChild.Position].Selected = true;
            recordsPacheteTuristice();
        }

        private void recordsPacheteTuristice()
        {
            labelRecordsPacheteTuristice.Text = "Record " + (bsChild.Position + 1) + " of " + bsChild.Count;
        }

        private void buttonFirstPachetTuristic_Click(object sender, EventArgs e)
        {
            bsChild.MoveFirst();
            dataGridChildUpdate();
            recordsPacheteTuristice();
        }

        private void buttonPreviousPachetTuristic_Click(object sender, EventArgs e)
        {
            bsChild.MovePrevious();
            dataGridChildUpdate();
            recordsPacheteTuristice();
        }

        private void buttonNextPachetTuristic_Click(object sender, EventArgs e)
        {
            bsChild.MoveNext();
            dataGridChildUpdate();
            recordsPacheteTuristice();
        }

        private void buttonLastPachetTuristic_Click(object sender, EventArgs e)
        {
            bsChild.MoveLast();
            dataGridChildUpdate();
            recordsPacheteTuristice();
        }
    }
}
