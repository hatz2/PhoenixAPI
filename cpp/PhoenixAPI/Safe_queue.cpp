#include "Safe_queue.h"

void Phoenix::Safe_queue::push(const std::string& message)
{
    size_t length = message.size();
    char* message_copy = new char[length + 1];
    memcpy(message_copy, message.c_str(), length);
    message_copy[length] = '\0';

    std::lock_guard<std::mutex> lock(mutex);
    queue.push(message_copy);
}

void Phoenix::Safe_queue::pop()
{
    std::lock_guard<std::mutex> lock(mutex);
    char* message = queue.front();
    queue.pop();
    delete[] message;
}

std::string Phoenix::Safe_queue::front()
{
    std::lock_guard<std::mutex> lock(mutex);
    char* message = queue.front();

    return std::string(message);
}

bool Phoenix::Safe_queue::empty()
{
    std::lock_guard<std::mutex> lock(mutex);
    return queue.empty();
}
