#pragma once

#include "PhoenixApi/Api.h"

class Module
{
public:
    virtual void on_send(const std::vector<std::string>& packet_splitted) {}
    virtual void on_recv(const std::vector<std::string>& packet_splitted) {}
};

