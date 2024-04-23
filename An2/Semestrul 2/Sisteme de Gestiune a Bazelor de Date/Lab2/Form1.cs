using Microsoft.Data.SqlClient;
using System;
using System.Data;
using System.Windows.Forms;
using System.Configuration;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Data.Common;

namespace Lab2
{
    public partial class Form1 : Form
    {
        DataSet ds = new DataSet();
        SqlDataAdapter daParent = new SqlDataAdapter();
        SqlDataAdapter daChild = new SqlDataAdapter();

        string ParentTableName = ConfigurationManager.AppSettings["ParentTableName"];
        string ChildTableName = ConfigurationManager.AppSettings["ChildTableName"];

        string ChildColumnNames = ConfigurationManager.AppSettings["ChildColumnNames"];
        List<string> ColumnNamesList = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));
        string ColumnNamesInsertParameters = ConfigurationManager.AppSettings["ColumnNamesInsertParameters"];

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string con = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;
            SqlConnection cs = new SqlConnection(con);

            string selectFromParent = ConfigurationSettings.AppSettings["selectFromParent"];
            daParent.SelectCommand = new SqlCommand(selectFromParent, cs);
            ds.Clear();
            daParent.Fill(ds, ParentTableName);
            dataGridParent.DataSource = ds.Tables[ParentTableName];

            dataGridParent.SelectionChanged += DataGridParent_SelectionChanged;
            dataGridChild.SelectionChanged += dataGridChild_SelectionChanged;

            int labelY = 5; // Initial Y position for labels
            int textFieldY = 5; // Initial Y position for text fields

            foreach (string columnName in ColumnNamesList.Skip(1).Take(ColumnNamesList.Count - 2))
            {
                Label label = new Label();
                label.Text = columnName + ":";
                label.AutoSize = true;
                label.Location = new Point(0, labelY);
                label.Font = new Font("Microsoft PhagsPa", 11.25f, FontStyle.Regular);

                TextBox textField = new TextBox();
                textField.Name = columnName;
                textField.Location = new Point(110, textFieldY);
                textField.Width = 200;

                panel1.Controls.Add(label);
                panel1.Controls.Add(textField);

                labelY += 30;
                textFieldY += 30;
            }
        }

        private void DataGridParent_SelectionChanged(object sender, EventArgs e)
        {
            if (dataGridParent.SelectedRows.Count > 0)
            {
                DataRowView selectedRow = dataGridParent.SelectedRows[0].DataBoundItem as DataRowView;
                int parentId = Convert.ToInt32(selectedRow[0]);

                string con = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;
                SqlConnection cs = new SqlConnection(con);

                string selectFromChild = ConfigurationSettings.AppSettings["selectFromChild"];

                SqlCommand cmd = new SqlCommand(selectFromChild, cs);
                cmd.Parameters.AddWithValue("@ID", parentId);

                if (ds.Tables.Contains(ChildTableName))
                {
                    ds.Tables[ChildTableName].Clear();
                }

                daChild.SelectCommand = cmd;
                daChild.Fill(ds, ChildTableName);
                dataGridChild.DataSource = ds.Tables[ChildTableName];
            }
        }

        private void dataGridChild_SelectionChanged(object sender, EventArgs e)
        {
            if (dataGridChild.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedRow = dataGridChild.SelectedRows[0];

                foreach (Control control in panel1.Controls)
                {
                    if (control is TextBox)
                    {
                        string columnName = control.Name;

                        if (selectedRow.Cells[columnName] != null)
                        {
                            control.Text = selectedRow.Cells[columnName].Value.ToString();
                        }
                    }
                }
            }
        }

        private void buttonReload_Click(object sender, EventArgs e)
        {
            string con = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;
            SqlConnection cs = new SqlConnection(con);

            // Reload parent data
            string selectFromParent = ConfigurationSettings.AppSettings["selectFromParent"];
            daParent.SelectCommand = new SqlCommand(selectFromParent, cs);
            ds.Clear();
            daParent.Fill(ds, ParentTableName);

            // Reload child data if there's a parent row selected
            if (dataGridParent.SelectedRows.Count > 0)
            {
                DataRowView selectedRow = dataGridParent.SelectedRows[0].DataBoundItem as DataRowView;
                int parentId = Convert.ToInt32(selectedRow[0]);

                string selectFromChild = ConfigurationSettings.AppSettings["selectFromChild"];

                SqlCommand cmd = new SqlCommand(selectFromChild, cs);
                cmd.Parameters.AddWithValue("@ID", parentId);

                ds.Tables[ChildTableName].Clear();
                daChild.SelectCommand = cmd;
                daChild.Fill(ds, ChildTableName);
            }

            dataGridParent.DataSource = ds.Tables[ParentTableName];
            dataGridChild.DataSource = ds.Tables[ChildTableName];

            foreach (Control control in panel1.Controls)
            {
                if (control is TextBox)
                {
                    control.Text = string.Empty;
                }
            }
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            try
            {
                string con = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;
                SqlConnection cs = new SqlConnection(con);
                cs.Open();

                SqlCommand cmd = new SqlCommand("INSERT INTO " + ChildTableName + " (" + ChildColumnNames + ") VALUES (" + ColumnNamesInsertParameters + ")", cs);

                string maxIdCommand = ConfigurationSettings.AppSettings["maxIdCommand"];
                SqlCommand getMaxIdCommand = new SqlCommand(maxIdCommand, cs);
                int maxId = Convert.ToInt32(getMaxIdCommand.ExecuteScalar());
                int id = maxId + 1;

                DataRowView selectedParentRow = dataGridParent.SelectedRows[0].DataBoundItem as DataRowView;
                int parentId = Convert.ToInt32(selectedParentRow[0]);

                cmd.Parameters.AddWithValue("@id", id);
                cmd.Parameters.AddWithValue("@parentId", parentId);

                int pos = 1;
                List<string> ColumnNamesInsertParametersList = new List<string>(ConfigurationManager.AppSettings["ColumnNamesInsertParameters"].Split(','));
                foreach (string column in ColumnNamesList.Skip(1).Take(ColumnNamesList.Count - 2))
                {
                    TextBox textBox = (TextBox)panel1.Controls[column];
                    cmd.Parameters.AddWithValue(ColumnNamesInsertParametersList[pos], textBox.Text);
                    pos++;
                }

                // Execute the command
                cmd.ExecuteNonQuery();

                // Refresh the child DataGridView
                if (ds.Tables.Contains(ChildTableName))
                {
                    ds.Tables[ChildTableName].Clear();
                }
                daChild.Fill(ds, ChildTableName);
                dataGridChild.DataSource = ds.Tables[ChildTableName];

                cs.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error occurred: " + ex.Message);
            }
        }

        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            try
            {
                string con = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;
                SqlConnection cs = new SqlConnection(con);
                cs.Open();

                string update = ConfigurationSettings.AppSettings["UpdateQuery"];
                SqlCommand cmd = new SqlCommand(update, cs);

                DataGridViewRow selectedRow = dataGridChild.SelectedRows[0];
                int id = Convert.ToInt32(selectedRow.Cells[0].Value);
                cmd.Parameters.AddWithValue("@id", id);

                int pos = 1;
                List<string> ColumnNamesInsertParametersList = new List<string>(ConfigurationManager.AppSettings["ColumnNamesInsertParameters"].Split(','));
                foreach (string column in ColumnNamesList.Skip(1).Take(ColumnNamesList.Count - 2))
                {
                    TextBox textBox = (TextBox)panel1.Controls[column];
                    cmd.Parameters.AddWithValue(ColumnNamesInsertParametersList[pos], textBox.Text);
                    pos++;
                }

                // Execute the command
                cmd.ExecuteNonQuery();

                // Refresh the child DataGridView
                if (ds.Tables.Contains(ChildTableName))
                {
                    ds.Tables[ChildTableName].Clear();
                }
                daChild.Fill(ds, ChildTableName);
                dataGridChild.DataSource = ds.Tables[ChildTableName];

                cs.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error occurred: " + ex.Message);
            }
        }

        private void buttonDelete_Click(object sender, EventArgs e)
        {
            try
            {
                string con = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;
                SqlConnection cs = new SqlConnection(con);
                cs.Open();

                string delete = ConfigurationSettings.AppSettings["DeleteQuery"];
                SqlCommand cmd = new SqlCommand(delete, cs);

                DataGridViewRow selectedRow = dataGridChild.SelectedRows[0];
                int id = Convert.ToInt32(selectedRow.Cells[0].Value);
                cmd.Parameters.AddWithValue("@id", id);

                // Execute the command
                cmd.ExecuteNonQuery();

                // Refresh the child DataGridView
                if (ds.Tables.Contains(ChildTableName))
                {
                    ds.Tables[ChildTableName].Clear();
                }
                daChild.Fill(ds, ChildTableName);
                dataGridChild.DataSource = ds.Tables[ChildTableName];

                cs.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error occurred: " + ex.Message);
            }
        }
    }
}
