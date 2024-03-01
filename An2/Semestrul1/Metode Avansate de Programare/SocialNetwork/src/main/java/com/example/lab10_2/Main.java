package com.example.lab10_2;

import com.example.lab10_2.domain.Message;
import com.example.lab10_2.domain.validators.FriendshipValidator;
import com.example.lab10_2.domain.validators.UserValidator;
import com.example.lab10_2.repository.*;
import com.example.lab10_2.service.Service;
import com.example.lab10_2.ui.ConsoleUI;

public class Main {

    public static void main(String[] args) {
        UserRepository userRepo = new UserDbRepository("jdbc:postgresql://localhost:5432/socialnetwork", "postgres", "postgres", new UserValidator());
        FriendshipRepository friendshipRepo = new FriendshipDbRepository("jdbc:postgresql://localhost:5432/socialnetwork", "postgres", "postgres", new FriendshipValidator());
        Repository<Long, Message> messageRepo = new MessageDbRepository("jdbc:postgresql://localhost:5432/socialnetwork", "postgres", "postgres", userRepo);
        //InMemoryRepository<UUID, User> userRepo = new InMemoryRepository<>(new UserValidator());
        //InMemoryRepository<UUID, Friendship> friendshipRepo = new InMemoryRepository<>(new FriendshipValidator());

        Service srv = new Service(userRepo, friendshipRepo, messageRepo);
        ConsoleUI console = new ConsoleUI(srv);

        console.run();
    }
}
