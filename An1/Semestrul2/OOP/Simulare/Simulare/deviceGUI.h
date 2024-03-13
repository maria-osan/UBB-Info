#pragma once

#include "service.h"

#include <QtWidgets>

class serviceGUI : public QWidget {
private:
	Service& srv;

	QListWidget* lst = new QListWidget;

	QPushButton* btnSortAn = new QPushButton{ "Sortare An" };
	QPushButton* btnSortModel = new QPushButton{ "Sortare Model" };
	QPushButton* btnNeSort = new QPushButton{ "Nesortate" };
	QPushButton* btnAdd = new QPushButton{ "Adaugare" };

	QLineEdit* txtId = new QLineEdit;
	QLineEdit* txtSerie = new QLineEdit;
	QLineEdit* txtModel = new QLineEdit;
	QLineEdit* txtTip = new QLineEdit;
	QLineEdit* txtCuloare = new QLineEdit;
	QLineEdit* txtAn = new QLineEdit;
	QLineEdit* txtPret = new QLineEdit;

	void initGUI();
	void loadList(const vector<Device>& all);
	void connectSignals();

public:
	serviceGUI(Service& srv) :srv{ srv } {
		initGUI();
		loadList(srv.get_all_dev());
		connectSignals();
	}
};