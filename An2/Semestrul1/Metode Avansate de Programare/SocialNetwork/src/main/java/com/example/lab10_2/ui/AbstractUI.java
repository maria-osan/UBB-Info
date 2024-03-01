package com.example.lab10_2.ui;

import com.example.lab10_2.service.ServiceInterface;

public abstract class AbstractUI implements UI{
    ServiceInterface srv;

    public AbstractUI(ServiceInterface srv) {
        this.srv = srv;
    }
}
