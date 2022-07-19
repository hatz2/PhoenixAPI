#pragma once
#include <iostream>
#include <string>
#include <mutex>

namespace Logger
{
    void print(const std::string& text);
    void error(const std::string& text);
}