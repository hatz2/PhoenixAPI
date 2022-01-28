#pragma once

#include "Module.h"
#include <map>
#include <set>

class Scene : public Module
{
public:
    void on_recv(const std::vector<std::string>& packet_splitted, const std::string& full_packet);

    size_t get_items_count() const;
    const std::set<int> get_items() const;

private:
    void handle_out(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_drop(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_get(const std::vector<std::string>& packet_splitted, const std::string& full_packet);
    void handle_cmap(const std::vector<std::string>& packet_splitted, const std::string& full_packet);

    std::set<int /* id */> items;
};

