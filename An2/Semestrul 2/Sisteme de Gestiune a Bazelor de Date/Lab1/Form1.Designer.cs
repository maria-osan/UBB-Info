namespace Lab1
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dataGridParent = new System.Windows.Forms.DataGridView();
            this.dataGridChild = new System.Windows.Forms.DataGridView();
            this.labelDestinatii = new System.Windows.Forms.Label();
            this.labelPacheteTuristice = new System.Windows.Forms.Label();
            this.textBoxNumePachet = new System.Windows.Forms.TextBox();
            this.labelNumePachet = new System.Windows.Forms.Label();
            this.labelDescriere = new System.Windows.Forms.Label();
            this.labelPret = new System.Windows.Forms.Label();
            this.textBoxDescriere = new System.Windows.Forms.TextBox();
            this.textBoxPret = new System.Windows.Forms.TextBox();
            this.buttonReload = new System.Windows.Forms.Button();
            this.buttonAdd = new System.Windows.Forms.Button();
            this.buttonUpdate = new System.Windows.Forms.Button();
            this.buttonDelete = new System.Windows.Forms.Button();
            this.labelRecordsDestinatii = new System.Windows.Forms.Label();
            this.labelRecordsPacheteTuristice = new System.Windows.Forms.Label();
            this.buttonFirstDestinatie = new System.Windows.Forms.Button();
            this.buttonPreviousDestinatie = new System.Windows.Forms.Button();
            this.buttonNextDestinatie = new System.Windows.Forms.Button();
            this.buttonLastDestinatie = new System.Windows.Forms.Button();
            this.buttonFirstPachetTuristic = new System.Windows.Forms.Button();
            this.buttonPreviousPachetTuristic = new System.Windows.Forms.Button();
            this.buttonNextPachetTuristic = new System.Windows.Forms.Button();
            this.buttonLastPachetTuristic = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridParent)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridChild)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridParent
            // 
            this.dataGridParent.BackgroundColor = System.Drawing.SystemColors.GradientActiveCaption;
            this.dataGridParent.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridParent.GridColor = System.Drawing.SystemColors.GradientInactiveCaption;
            this.dataGridParent.Location = new System.Drawing.Point(50, 45);
            this.dataGridParent.Name = "dataGridParent";
            this.dataGridParent.RowHeadersWidth = 80;
            this.dataGridParent.Size = new System.Drawing.Size(600, 150);
            this.dataGridParent.TabIndex = 0;
            // 
            // dataGridChild
            // 
            this.dataGridChild.BackgroundColor = System.Drawing.SystemColors.GradientActiveCaption;
            this.dataGridChild.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridChild.GridColor = System.Drawing.SystemColors.GradientInactiveCaption;
            this.dataGridChild.Location = new System.Drawing.Point(50, 265);
            this.dataGridChild.Margin = new System.Windows.Forms.Padding(0);
            this.dataGridChild.Name = "dataGridChild";
            this.dataGridChild.RowHeadersWidth = 100;
            this.dataGridChild.Size = new System.Drawing.Size(600, 80);
            this.dataGridChild.TabIndex = 1;
            // 
            // labelDestinatii
            // 
            this.labelDestinatii.AutoSize = true;
            this.labelDestinatii.Font = new System.Drawing.Font("Microsoft PhagsPa", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelDestinatii.Location = new System.Drawing.Point(50, 20);
            this.labelDestinatii.Name = "labelDestinatii";
            this.labelDestinatii.Size = new System.Drawing.Size(88, 21);
            this.labelDestinatii.TabIndex = 2;
            this.labelDestinatii.Text = "Destinatii:";
            // 
            // labelPacheteTuristice
            // 
            this.labelPacheteTuristice.AutoSize = true;
            this.labelPacheteTuristice.Font = new System.Drawing.Font("Microsoft PhagsPa", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelPacheteTuristice.Location = new System.Drawing.Point(50, 240);
            this.labelPacheteTuristice.Name = "labelPacheteTuristice";
            this.labelPacheteTuristice.Size = new System.Drawing.Size(140, 21);
            this.labelPacheteTuristice.TabIndex = 3;
            this.labelPacheteTuristice.Text = "PacheteTuristice:";
            // 
            // textBoxNumePachet
            // 
            this.textBoxNumePachet.Location = new System.Drawing.Point(165, 420);
            this.textBoxNumePachet.Name = "textBoxNumePachet";
            this.textBoxNumePachet.Size = new System.Drawing.Size(165, 20);
            this.textBoxNumePachet.TabIndex = 4;
            // 
            // labelNumePachet
            // 
            this.labelNumePachet.AutoSize = true;
            this.labelNumePachet.Font = new System.Drawing.Font("Microsoft PhagsPa", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelNumePachet.Location = new System.Drawing.Point(50, 420);
            this.labelNumePachet.Name = "labelNumePachet";
            this.labelNumePachet.Size = new System.Drawing.Size(101, 20);
            this.labelNumePachet.TabIndex = 5;
            this.labelNumePachet.Text = "Nume pachet:";
            // 
            // labelDescriere
            // 
            this.labelDescriere.AutoSize = true;
            this.labelDescriere.Font = new System.Drawing.Font("Microsoft PhagsPa", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelDescriere.Location = new System.Drawing.Point(50, 450);
            this.labelDescriere.Name = "labelDescriere";
            this.labelDescriere.Size = new System.Drawing.Size(74, 20);
            this.labelDescriere.TabIndex = 6;
            this.labelDescriere.Text = "Descriere:";
            // 
            // labelPret
            // 
            this.labelPret.AutoSize = true;
            this.labelPret.Font = new System.Drawing.Font("Microsoft PhagsPa", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelPret.Location = new System.Drawing.Point(50, 480);
            this.labelPret.Name = "labelPret";
            this.labelPret.Size = new System.Drawing.Size(38, 20);
            this.labelPret.TabIndex = 7;
            this.labelPret.Text = "Pret:";
            // 
            // textBoxDescriere
            // 
            this.textBoxDescriere.Location = new System.Drawing.Point(165, 450);
            this.textBoxDescriere.Name = "textBoxDescriere";
            this.textBoxDescriere.Size = new System.Drawing.Size(165, 20);
            this.textBoxDescriere.TabIndex = 8;
            // 
            // textBoxPret
            // 
            this.textBoxPret.Location = new System.Drawing.Point(165, 480);
            this.textBoxPret.Name = "textBoxPret";
            this.textBoxPret.Size = new System.Drawing.Size(165, 20);
            this.textBoxPret.TabIndex = 9;
            // 
            // buttonReload
            // 
            this.buttonReload.Font = new System.Drawing.Font("Microsoft PhagsPa", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonReload.Location = new System.Drawing.Point(550, 480);
            this.buttonReload.Name = "buttonReload";
            this.buttonReload.Size = new System.Drawing.Size(100, 25);
            this.buttonReload.TabIndex = 10;
            this.buttonReload.Text = "Reload data";
            this.buttonReload.UseVisualStyleBackColor = true;
            this.buttonReload.Click += new System.EventHandler(this.buttonReload_Click);
            // 
            // buttonAdd
            // 
            this.buttonAdd.BackColor = System.Drawing.SystemColors.ButtonHighlight;
            this.buttonAdd.Font = new System.Drawing.Font("Microsoft PhagsPa", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonAdd.Location = new System.Drawing.Point(395, 420);
            this.buttonAdd.Name = "buttonAdd";
            this.buttonAdd.Size = new System.Drawing.Size(75, 25);
            this.buttonAdd.TabIndex = 11;
            this.buttonAdd.Text = "Add";
            this.buttonAdd.UseVisualStyleBackColor = false;
            this.buttonAdd.Click += new System.EventHandler(this.buttonAdd_Click);
            // 
            // buttonUpdate
            // 
            this.buttonUpdate.BackColor = System.Drawing.SystemColors.ButtonHighlight;
            this.buttonUpdate.Font = new System.Drawing.Font("Microsoft PhagsPa", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonUpdate.Location = new System.Drawing.Point(485, 420);
            this.buttonUpdate.Name = "buttonUpdate";
            this.buttonUpdate.Size = new System.Drawing.Size(75, 25);
            this.buttonUpdate.TabIndex = 12;
            this.buttonUpdate.Text = "Update";
            this.buttonUpdate.UseVisualStyleBackColor = false;
            this.buttonUpdate.Click += new System.EventHandler(this.buttonUpdate_Click);
            // 
            // buttonDelete
            // 
            this.buttonDelete.BackColor = System.Drawing.SystemColors.ButtonHighlight;
            this.buttonDelete.Font = new System.Drawing.Font("Microsoft PhagsPa", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.buttonDelete.Location = new System.Drawing.Point(575, 420);
            this.buttonDelete.Name = "buttonDelete";
            this.buttonDelete.Size = new System.Drawing.Size(75, 25);
            this.buttonDelete.TabIndex = 13;
            this.buttonDelete.Text = "Delete";
            this.buttonDelete.UseVisualStyleBackColor = false;
            this.buttonDelete.Click += new System.EventHandler(this.buttonDelete_Click);
            // 
            // labelRecordsDestinatii
            // 
            this.labelRecordsDestinatii.AutoSize = true;
            this.labelRecordsDestinatii.Location = new System.Drawing.Point(50, 205);
            this.labelRecordsDestinatii.Name = "labelRecordsDestinatii";
            this.labelRecordsDestinatii.Size = new System.Drawing.Size(66, 13);
            this.labelRecordsDestinatii.TabIndex = 14;
            this.labelRecordsDestinatii.Text = "Record 1 of ";
            // 
            // labelRecordsPacheteTuristice
            // 
            this.labelRecordsPacheteTuristice.AutoSize = true;
            this.labelRecordsPacheteTuristice.Location = new System.Drawing.Point(50, 355);
            this.labelRecordsPacheteTuristice.Name = "labelRecordsPacheteTuristice";
            this.labelRecordsPacheteTuristice.Size = new System.Drawing.Size(63, 13);
            this.labelRecordsPacheteTuristice.TabIndex = 15;
            this.labelRecordsPacheteTuristice.Text = "Record 1 of";
            // 
            // buttonFirstDestinatie
            // 
            this.buttonFirstDestinatie.Location = new System.Drawing.Point(305, 205);
            this.buttonFirstDestinatie.Name = "buttonFirstDestinatie";
            this.buttonFirstDestinatie.Size = new System.Drawing.Size(75, 25);
            this.buttonFirstDestinatie.TabIndex = 16;
            this.buttonFirstDestinatie.Text = "First";
            this.buttonFirstDestinatie.UseVisualStyleBackColor = true;
            this.buttonFirstDestinatie.Click += new System.EventHandler(this.buttonFirstDestinatie_Click);
            // 
            // buttonPreviousDestinatie
            // 
            this.buttonPreviousDestinatie.Location = new System.Drawing.Point(395, 205);
            this.buttonPreviousDestinatie.Name = "buttonPreviousDestinatie";
            this.buttonPreviousDestinatie.Size = new System.Drawing.Size(75, 25);
            this.buttonPreviousDestinatie.TabIndex = 17;
            this.buttonPreviousDestinatie.Text = "Previous";
            this.buttonPreviousDestinatie.UseVisualStyleBackColor = true;
            this.buttonPreviousDestinatie.Click += new System.EventHandler(this.buttonPreviousDestinatie_Click);
            // 
            // buttonNextDestinatie
            // 
            this.buttonNextDestinatie.Location = new System.Drawing.Point(485, 205);
            this.buttonNextDestinatie.Name = "buttonNextDestinatie";
            this.buttonNextDestinatie.Size = new System.Drawing.Size(75, 25);
            this.buttonNextDestinatie.TabIndex = 18;
            this.buttonNextDestinatie.Text = "Next";
            this.buttonNextDestinatie.UseVisualStyleBackColor = true;
            this.buttonNextDestinatie.Click += new System.EventHandler(this.buttonNextDestinatie_Click);
            // 
            // buttonLastDestinatie
            // 
            this.buttonLastDestinatie.Location = new System.Drawing.Point(577, 205);
            this.buttonLastDestinatie.Name = "buttonLastDestinatie";
            this.buttonLastDestinatie.Size = new System.Drawing.Size(75, 25);
            this.buttonLastDestinatie.TabIndex = 19;
            this.buttonLastDestinatie.Text = "Last";
            this.buttonLastDestinatie.UseVisualStyleBackColor = true;
            this.buttonLastDestinatie.Click += new System.EventHandler(this.buttonLastDestinatie_Click);
            // 
            // buttonFirstPachetTuristic
            // 
            this.buttonFirstPachetTuristic.Location = new System.Drawing.Point(305, 355);
            this.buttonFirstPachetTuristic.Name = "buttonFirstPachetTuristic";
            this.buttonFirstPachetTuristic.Size = new System.Drawing.Size(75, 25);
            this.buttonFirstPachetTuristic.TabIndex = 20;
            this.buttonFirstPachetTuristic.Text = "First";
            this.buttonFirstPachetTuristic.UseVisualStyleBackColor = true;
            this.buttonFirstPachetTuristic.Click += new System.EventHandler(this.buttonFirstPachetTuristic_Click);
            // 
            // buttonPreviousPachetTuristic
            // 
            this.buttonPreviousPachetTuristic.Location = new System.Drawing.Point(395, 355);
            this.buttonPreviousPachetTuristic.Name = "buttonPreviousPachetTuristic";
            this.buttonPreviousPachetTuristic.Size = new System.Drawing.Size(75, 25);
            this.buttonPreviousPachetTuristic.TabIndex = 21;
            this.buttonPreviousPachetTuristic.Text = "Previous";
            this.buttonPreviousPachetTuristic.UseVisualStyleBackColor = true;
            this.buttonPreviousPachetTuristic.Click += new System.EventHandler(this.buttonPreviousPachetTuristic_Click);
            // 
            // buttonNextPachetTuristic
            // 
            this.buttonNextPachetTuristic.Location = new System.Drawing.Point(485, 355);
            this.buttonNextPachetTuristic.Name = "buttonNextPachetTuristic";
            this.buttonNextPachetTuristic.Size = new System.Drawing.Size(75, 25);
            this.buttonNextPachetTuristic.TabIndex = 22;
            this.buttonNextPachetTuristic.Text = "Next";
            this.buttonNextPachetTuristic.UseVisualStyleBackColor = true;
            this.buttonNextPachetTuristic.Click += new System.EventHandler(this.buttonNextPachetTuristic_Click);
            // 
            // buttonLastPachetTuristic
            // 
            this.buttonLastPachetTuristic.Location = new System.Drawing.Point(575, 355);
            this.buttonLastPachetTuristic.Name = "buttonLastPachetTuristic";
            this.buttonLastPachetTuristic.Size = new System.Drawing.Size(75, 25);
            this.buttonLastPachetTuristic.TabIndex = 23;
            this.buttonLastPachetTuristic.Text = "Last";
            this.buttonLastPachetTuristic.UseVisualStyleBackColor = true;
            this.buttonLastPachetTuristic.Click += new System.EventHandler(this.buttonLastPachetTuristic_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(701, 536);
            this.Controls.Add(this.buttonLastPachetTuristic);
            this.Controls.Add(this.buttonNextPachetTuristic);
            this.Controls.Add(this.buttonPreviousPachetTuristic);
            this.Controls.Add(this.buttonFirstPachetTuristic);
            this.Controls.Add(this.buttonLastDestinatie);
            this.Controls.Add(this.buttonNextDestinatie);
            this.Controls.Add(this.buttonPreviousDestinatie);
            this.Controls.Add(this.buttonFirstDestinatie);
            this.Controls.Add(this.labelRecordsPacheteTuristice);
            this.Controls.Add(this.labelRecordsDestinatii);
            this.Controls.Add(this.buttonDelete);
            this.Controls.Add(this.buttonUpdate);
            this.Controls.Add(this.buttonAdd);
            this.Controls.Add(this.buttonReload);
            this.Controls.Add(this.textBoxPret);
            this.Controls.Add(this.textBoxDescriere);
            this.Controls.Add(this.labelPret);
            this.Controls.Add(this.labelDescriere);
            this.Controls.Add(this.labelNumePachet);
            this.Controls.Add(this.textBoxNumePachet);
            this.Controls.Add(this.labelPacheteTuristice);
            this.Controls.Add(this.labelDestinatii);
            this.Controls.Add(this.dataGridChild);
            this.Controls.Add(this.dataGridParent);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridParent)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridChild)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dataGridParent;
        private System.Windows.Forms.DataGridView dataGridChild;
        private System.Windows.Forms.Label labelDestinatii;
        private System.Windows.Forms.Label labelPacheteTuristice;
        private System.Windows.Forms.TextBox textBoxNumePachet;
        private System.Windows.Forms.Label labelNumePachet;
        private System.Windows.Forms.Label labelDescriere;
        private System.Windows.Forms.Label labelPret;
        private System.Windows.Forms.TextBox textBoxDescriere;
        private System.Windows.Forms.TextBox textBoxPret;
        private System.Windows.Forms.Button buttonReload;
        private System.Windows.Forms.Button buttonAdd;
        private System.Windows.Forms.Button buttonUpdate;
        private System.Windows.Forms.Button buttonDelete;
        private System.Windows.Forms.Label labelRecordsDestinatii;
        private System.Windows.Forms.Label labelRecordsPacheteTuristice;
        private System.Windows.Forms.Button buttonFirstDestinatie;
        private System.Windows.Forms.Button buttonPreviousDestinatie;
        private System.Windows.Forms.Button buttonNextDestinatie;
        private System.Windows.Forms.Button buttonLastDestinatie;
        private System.Windows.Forms.Button buttonFirstPachetTuristic;
        private System.Windows.Forms.Button buttonPreviousPachetTuristic;
        private System.Windows.Forms.Button buttonNextPachetTuristic;
        private System.Windows.Forms.Button buttonLastPachetTuristic;
    }
}

