#include "Split_string.h"

std::vector<std::string> split_string(const std::string& str, char delimiter)
{
    std::vector<std::string> splitted_string;

    size_t start = 0U;
    size_t end = str.find(delimiter);

    while (end != std::string::npos)
    {
        splitted_string.push_back(str.substr(start, end - start));
        start = end + sizeof(char);
        end = str.find(delimiter, start);
    }

    splitted_string.push_back(str.substr(start, end));

    return splitted_string;
}
