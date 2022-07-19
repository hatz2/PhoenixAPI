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

bool Phoenix::Api::send_packet(const std::string& packet)
{
    nlohmann::json json_data;
    json_data["type"] = Type::packet_send;
    json_data["packet"] = packet;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::recv_packet(const std::string& packet)
{
    nlohmann::json json_data;
    json_data["type"] = Type::packet_recv;
    json_data["packet"] = packet;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::attack_monster(int monster_id)
{
    nlohmann::json json_data;
    json_data["type"] = Type::attack;
    json_data["monster_id"] = monster_id;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::use_player_skill(int monster_id, int skill_id)
{
    nlohmann::json json_data;
    json_data["type"] = Type::player_skill;
    json_data["monster_id"] = monster_id;
    json_data["skill_id"] = skill_id;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::player_walk(int x, int y)
{
    nlohmann::json json_data;
    json_data["type"] = Type::player_walk;
    json_data["x"] = x;
    json_data["y"] = y;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::use_pet_skill(int monster_id, int skill_id)
{
    nlohmann::json json_data;
    json_data["type"] = Type::pet_skill;
    json_data["monster_id"] = monster_id;
    json_data["skill_id"] = skill_id;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::use_partner_skill(int monster_id, int skill_id)
{
    nlohmann::json json_data;
    json_data["type"] = Type::partner_skill;
    json_data["monster_id"] = monster_id;
    json_data["skill_id"] = skill_id;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::pets_walk(int x, int y)
{
    nlohmann::json json_data;
    json_data["type"] = Type::pets_walk;
    json_data["x"] = x;
    json_data["y"] = y;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::pick_up(int item_id)
{
    nlohmann::json json_data;
    json_data["type"] = Type::pick_up;
    json_data["item_id"] = item_id;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::collect(int npc_id)
{
    nlohmann::json json_data;
    json_data["type"] = Type::collect;
    json_data["npc_id"] = npc_id;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::start_bot()
{
    nlohmann::json json_data;
    json_data["type"] = Type::start_bot;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::stop_bot()
{
    nlohmann::json json_data;
    json_data["type"] = Type::stop_bot;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::continue_bot()
{
    nlohmann::json json_data;
    json_data["type"] = Type::continue_bot;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::load_settings(const std::string& settings_path)
{
    nlohmann::json json_data;
    json_data["type"] = Type::load_settings;
    json_data["path"] = settings_path;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::start_minigame_bot()
{
    nlohmann::json json_data;
    json_data["type"] = Type::start_minigame_bot;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
}

bool Phoenix::Api::stop_minigame_bot()
{
    nlohmann::json json_data;
    json_data["type"] = Type::stop_minigame_bot;

    return (send_data(json_data.dump()) != SOCKET_ERROR);
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

    sockaddr_in addr;
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
