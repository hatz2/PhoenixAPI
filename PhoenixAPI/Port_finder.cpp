#include "Port_finder.h"
#include <Windows.h>
#include <string>

static std::vector<int> ports;

BOOL CALLBACK enum_windows_callback(HWND hwnd, LPARAM param)
{
    const int title_size = GetWindowTextLengthA(hwnd);

    if (title_size <= 0)
    {
        return TRUE;
    }

    char* title = new char[title_size + 1];
    GetWindowTextA(hwnd, title, title_size + 1);

    std::string title_wrapper(title);

    if (title_wrapper.find("] - Phoenix Bot:") == std::string::npos)
    {
        delete[] title;
        return TRUE;
    }

    std::string port = title_wrapper.substr(title_wrapper.find_last_of(':') + 1);

    if (port.empty())
    {
        delete[] title;
        return TRUE;
    }

    ports.push_back(std::stoi(port));

    delete[] title;
    return TRUE;
}

std::vector<int> Phoenix::find_ports()
{
    ports.clear();

    EnumWindows(enum_windows_callback, 0);

    return ports;
}
