#include "Logger.h"

namespace
{
    std::mutex mtx;
}

void Logger::print(const std::string& text)
{
    std::lock_guard<std::mutex> lock(mtx);
    std::cout << text;
}

void Logger::error(const std::string& text)
{
    std::lock_guard<std::mutex> lock(mtx);
    std::cerr << text;
}
