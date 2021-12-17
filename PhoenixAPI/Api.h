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

	class Api
	{
	public:
		explicit Api(int port);
		~Api();

		int send_data(const std::string& data);

		bool empty();

		std::string get_message();

	private:
		void receive_messages();

		void initialize_socket(int port);

		static int instance_counter;
		SOCKET sock;
		sockaddr_in addr;
		Safe_queue messages;
		std::thread recv_thread;
		bool run;
	};
}



