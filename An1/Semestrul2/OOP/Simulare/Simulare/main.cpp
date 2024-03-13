#include <QtWidgets/QApplication>

#include "device.h"
#include "repo.h"
#include "service.h"
#include "deviceGUI.h"

void runGUI(int argc, char* argv[])
{
    QApplication a(argc, argv);

    RepoFile r{ "device.txt" };
    Service srv{ r };

    serviceGUI gui{ srv };
    gui.show();
    
    a.exec();
}

int main(int argc, char *argv[])
{
    test_all();

    runGUI(argc, argv);

    return 0;
}
