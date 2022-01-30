/*********************************************************************
 * @file   Api.h
 * @brief  Main file of the Phoenix Bot API
 *
 * @author Hatz
 * @date   December 2021
 *********************************************************************/

#pragma once

#include "Port_finder.h"
#include "Safe_queue.h"
#include <WinSock2.h>
#include <WS2tcpip.h>
#include <iostream>
#include <thread>
#include <nlohmann/json.hpp>

#pragma comment(lib, "ws2_32.lib")

namespace Phoenix
{
    /**
     * @brief Represents the type of messages that we can send/receive from the bot.
     */
    enum class Type
    {
        packet_send,
        packet_recv,
        attack,
        player_skill,
        player_walk,
        pet_skill,
        partner_skill,
        pets_walk,
        pick_up,
        collect,
        start_bot,
        stop_bot,
        continue_bot,
        load_settings,
        start_minigame_bot,
        stop_minigame_bot
    };

    /**
     * @brief Class that handles the main logic of the API.
     * It connects to the given port and receive the messages from
     * the bot in a thread safe queue.
     */
    class Api
    {
    public:
        /**
         * @brief Constructor.
         * @param port The port of the bot you want to connect
         */
        explicit Api(int port);

        /**
         * @brief Destructor.
         */
        ~Api();

        /**
         * @brief Send data to the bot.
         * @param data The data to send, it must be a valid JSON string
         * @return If no error then returns the number of bytes sent, otherwise it returns SOCKET_ERROR
         */
        int send_data(const std::string& data);

        /**
         * @brief Check if there is any message to read from the port.
         * @return true or false
         */
        bool empty();

        /**
         * @brief Get a message from the bot and pops it from the queue.
         * @return The first message in the queue.
         */
        std::string get_message();

        /**
         * @brief Wrapper to send a packet
         * @param packet The packet you want to send
         * @return false if there's any error, true otherwise
         */
        bool send_packet(const std::string& packet);

        /**
         * @brief Wrapper to receive a packet
         * @param packet The packet you want to receive
         * @return false if there's any error, true otherwise
         */
        bool recv_packet(const std::string& packet);

        /**
         * @brief Wrapper for attacking a monster with the skills set
         * in the bot
         * @param monster_id The id of the monster to attack
         * @return false if there's any error, true otherwise
         */
        bool attack_monster(int monster_id);

        /**
         * @brief Wrapper for attacking a monster with a specific skill
         * @param monster_id The id of the monster to attack
         * @param skill_id The id of the skill to use
         * @return false if there's any error, true otherwise
         */
        bool use_player_skill(int monster_id, int skill_id);

        /**
         * @brief Moves the player to a specific position
         * @return false if there's any error, true otherwise
         */
        bool player_walk(int x, int y);

        /**
         * @brief Attack a monster with a specific pet skill
         * @param monster_id The id of the monster to attack
         * @param skill_id The id of the skill to use
         * @return false if there's any error, true otherwise
         */
        bool use_pet_skill(int monster_id, int skill_id);

        /**
         * @brief Attack a monster with a specific partner skill
         * @param monster_id The id of the monster to attack
         * @param skill_id The id of the skill to use
         * @return false if there's any error, true otherwise
         */
        bool use_partner_skill(int monster_id, int skill_id);

        /**
         * @brief Moves both the pet and partner to a specific position
         * @return false if there's any error, true otherwise
         */
        bool pets_walk(int x, int y);

        /**
         * @brief Walk and pick up an item
         * @param item_id The id of the item to pick up
         * @return false if there's any error, true otherwise
         */
        bool pick_up(int item_id);

        /**
         * @brief Collect an npc (like ice flowers, grass, etc)
         * @param npc_id The id of the npc to collect
         * @return false if there's any error, true otherwise
         */
        bool collect(int npc_id);

        /**
         * @brief Start the farming bot
         */
        bool start_bot();

        /**
         * @brief Stop the farming bot
         */
        bool stop_bot();

        /**
         * @brief Continue the farming bot
         */
        bool continue_bot();

        /**
         * @brief Load a profile into the bot
         * @param settings_path The path to the .ini file
         * @return false if there's any error, true otherwise
         */
        bool load_settings(const std::string& settings_path);

        /**
         * @brief Starts the minigame bot
         * @return false if there's any error, true otherwise
         */
        bool start_minigame_bot();

        /**
         * @brief Stops the minigame bot
         * @return false if there's any error, true otherwise
         */
        bool stop_minigame_bot();

    private:
        /**
         * @brief Function that will be receiving all the messages
         * from the bot in a different thread.
         */
        void receive_messages();

        /**
         * @brief Initialize a socket connected to the given port
         * @param port The port to connect
         */
        void initialize_socket(int port);

        static int instance_counter;
        SOCKET sock;
        Safe_queue messages;
        std::thread recv_thread;
        bool run;
    };
}



