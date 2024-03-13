#include "deviceGUI.h"

void serviceGUI::initGUI()
{
	QHBoxLayout* main_ly = new QHBoxLayout;
	setLayout(main_ly);

	//partea stanga: lista de deviceuri
	main_ly->addWidget(lst);

	//partea dreapta: butoanele
	QVBoxLayout* btn_ly = new QVBoxLayout;

	QFormLayout* form_ly = new QFormLayout;
	form_ly->addRow("Serie", txtSerie);
	/*form_ly->addRow("Model", txtModel);
	form_ly->addRow("Tip", txtTip);
	form_ly->addRow("Culoare", txtCuloare);
	form_ly->addRow("An", txtAn);
	form_ly->addRow("Pret", txtPret);*/

	btn_ly->addLayout(form_ly);
	//btn_ly->addWidget(btnAdd);

	QHBoxLayout* sort_ly = new QHBoxLayout;
	sort_ly->addWidget(btnSortModel);
	sort_ly->addWidget(btnSortAn);

	btn_ly->addLayout(sort_ly);
	btn_ly->addWidget(btnNeSort);

	main_ly->addLayout(btn_ly);
}

void serviceGUI::loadList(const vector<Device>& all)
{
	txtId->clear();
	txtSerie->clear();
	txtModel->clear();
	txtTip->clear();
	txtCuloare->clear();
	txtAn->clear();
	txtPret->clear();

	lst->clear();

	for (const auto& d : all)
	{
		lst->addItem(QString::fromStdString(d.get_id()) + ": " + QString::fromStdString(d.get_model()) + ", " + QString::number(d.get_an()) + ", " + QString::number(d.get_pret()));
	}
}

void serviceGUI::connectSignals()
{
	QObject::connect(lst, &QListWidget::itemSelectionChanged, [&]() {
		auto sel = lst->selectedItems();
		if (sel.isEmpty())
		{
			txtSerie->setText("");
			txtModel->setText("");
			txtTip->setText("");
			txtCuloare->setText("");
			txtAn->setText("");
			txtPret->setText("");
		}
		else
		{
			auto selItem = sel.at(0);
			auto text = selItem->text().toStdString();
			string id;
			id.assign(text, 0, 2);
			auto d = srv.search(id);
			txtSerie->setText(QString::fromStdString(d.get_serie()));
			txtModel->setText(QString::fromStdString(d.get_model()));
			txtTip->setText(QString::fromStdString(d.get_tip()));
			txtCuloare->setText(QString::fromStdString(d.get_culoare()));
			txtAn->setText(QString::number(d.get_an()));
			txtPret->setText(QString::number(d.get_pret()));
		}
		});

	//butonul de sortare dupa model
	QObject::connect(btnSortModel, &QPushButton::clicked, [&]() {
		loadList(srv.sortModel());
		});

	//butonul de sortare dupa an
	QObject::connect(btnSortAn, &QPushButton::clicked, [&]() {
		loadList(srv.sortAn());
		});

	//butonul nesortate
	QObject::connect(btnNeSort, &QPushButton::clicked, [&]() {
		loadList(srv.get_all_dev());
		});
}