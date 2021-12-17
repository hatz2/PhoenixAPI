#include "Api.h"

int Phoenix::Api::instance_counter = 0;

Phoenix::Api::Api(int port) : run(true)
{
    initialize_socket(port);
    ++instance_counter;
    recv_thread = std::thread(&Api::receive_messages, this);
}

Phoenix::Api::~Api()
{
    if (recv_thread.joinable())
    {
        run = false;
        recv_thread.join();
    }

    --instance_counter;
    closesocket(sock);

    if (instance_counter == 0)
    {
        WSACleanup();
    }
}

int Phoenix::Api::send_data(const std::string& data)
{
    std::string msg = data + '\1';
    return send(sock, msg.c_str(), msg.size(), 0);
}

bool Phoenix::Api::empty()
{
    return messages.empty();
}

std::string Phoenix::Api::get_message()
{
    if (messages.empty())
    {
        return std::string();
    }

    std::string msg = messages.front();
    messages.pop();

    return msg;
}

void Phoenix::Api::receive_messages()
{
    constexpr int buffer_size = 4096;
    char buffer[buffer_size];
    std::string data;
    size_t delim_pos;

    while (run)
    {
        memset(buffer, 0, buffer_size);

        if (recv(sock, buffer, buffer_size - 1, 0) <= 0)
        {
            std::cerr << "recv failed\n";
            run = false;
            break;
        }

        data += buffer;

        while ((delim_pos = data.find('\1')) != std::string::npos)
        {
            std::string message = data.substr(0, delim_pos - 1);
            data.erase(0, delim_pos + 1);

            messages.push(message);
        }
    }
}

void Phoenix::Api::initialize_socket(int port)
{
    if (instance_counter == 0)
    {
        WSADATA wsa_data;

        if (WSAStartup(MAKEWORD(2, 2), &wsa_data) != 0)
        {
            std::cerr << "WSAStartup failed\n";
            exit(-1);
        }
    }

    sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

    if (sock == INVALID_SOCKET)
    {
        std::cerr << "socket failed\n";
        exit(-1);
    }

    inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr.s_addr);
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);

    if (connect(sock, reinterpret_cast<sockaddr*>(&addr), sizeof(sockaddr_in)) != 0)
    {
        std::cerr << "connect failed\n";
        closesocket(sock);
        WSACleanup();
        exit(-1);
    }
}
