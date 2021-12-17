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

#pragma comment(lib, "ws2_32.lib")

namespace Phoenix
{
	/**
	 * @brief Represents the type of messages that we can send/receive to the socket.
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
		collect
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
		 * @param The data to send, it must be a valid JSON string
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
		sockaddr_in addr;
		Safe_queue messages;
		std::thread recv_thread;
		bool run;
	};
}



