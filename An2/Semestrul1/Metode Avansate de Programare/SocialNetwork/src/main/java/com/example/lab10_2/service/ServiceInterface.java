package com.example.lab10_2.service;

import com.example.lab10_2.domain.FriendRequest;
import com.example.lab10_2.domain.Friendship;
import com.example.lab10_2.domain.Message;
import com.example.lab10_2.domain.User;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public interface ServiceInterface {
    /**
     * Add a user in the userRepo
     * @return true - successful operation
     *          false - otherwise
     */
    boolean addUser(String firstName, String lastName, String email);

    boolean addUser(User user);

    /**
     * Delete a user from userRepo by its email
     * @return the user with the given email - if it exists
     *          null - otherwise
     * ! Delete also all friendships that include that user
     */
    boolean deleteUser(String email);

    /**
     * Create a friendship between two users
     * @param email1 - the email of the first user
     * @param email2 - the email of the second user
     * @return true - if the friendship is added
     *          false - otherwise
     */
    boolean createFriendship(String email1, String email2);

    /**
     * Create a friend request between two users
     * @param email1 - the email number of the first user
     * @param email2 - the email number of the second user
     * @return true - if the friend request was created
     *          false - otherwise
     */
    boolean createFriendRequest(String email1, String email2);

    /**
     * Respond to a friendship request
     * @param friendshipReq - the friendship to be rejected
     * @return true - if the friend request got responded
     *          false - otherwise
     */
    boolean respondFriendRequest(Friendship friendshipReq, FriendRequest response);


    /**
     * Delete a friendship between two users
     * @param email1 - the email of the first user
     * @param email2 - the email of the second user
     * @return the friendship - if it is deleted
     *              false - otherwise
     */
    boolean deleteFriendship(String email1, String email2);

    /**
     * @return an Iterable of all the users
     */
    Iterable<User> getAllUsers();

    /**
     * @return an Iterable of all the friendships
     */
    Iterable<Friendship> getAllFriendships();

    /**
     * @return an Iterable of all the friendships
     */
    Iterable<Message> getAllMessages();

    /**
     * @return the number of communities - int
     */
    int numberOfCommunities();


    /**
     * Returns the most sociable community
     * the most sociable community is the community of users with the longest path
     *
     * @return an Iterable of all the most sociable communities users
     */
    List<List<User>> mostSociableCommunity();

    /**
     * @return a list of all the communities
     */
    List<List<User>> getAllCommunities();

    /**
     * @param email - the email of the searched user
     *
     * @return the user that has that specific email
     *          null - there is no such user
     */
    User getUserByEmail(String email);

    /**
     * Return the friendship between two users knowing their emails
     * @param email1 - the email of the first user
     * @param email2 - the email of the second user
     * @return the friendship - if it is found
     *          false - otherwise
     */
    Friendship getFriendshipByEmail(String email1, String email2);

    public ArrayList<Friendship> friendList(User user);

    ArrayList<Friendship> friendRequestList(User user);

    public Map<LocalDateTime, User> friendListFrom(User user, Integer month);

    /**
     * Add a message in the messageRepo
     */
    boolean addMessage(String email_from, List<String> emails_to, String message);
    boolean addMessage(String email_from, List<String> emails_to, String message, Message replyTo);

    ArrayList<Message> getMessagesBetweenTwoUsers(String user1, String user2);

    boolean updateMessage(Message msg);
}
