package com.example.lab10_2.controller;

import com.example.lab10_2.domain.FriendRequest;
import com.example.lab10_2.domain.Friendship;
import com.example.lab10_2.domain.Message;
import com.example.lab10_2.domain.User;
import com.example.lab10_2.dto.FriendshipFilterDTO;
import com.example.lab10_2.dto.UserFilterDTO;
import com.example.lab10_2.repository.Page;
import com.example.lab10_2.repository.Pageable;
import com.example.lab10_2.repository.Repository;
import com.example.lab10_2.service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

public class AppController {
    private Service srv;

    ObservableList<User> usersObs = FXCollections.observableArrayList();
    ObservableList<Friendship> friendshipsObs = FXCollections.observableArrayList();
    ObservableList<Message> messagesObs = FXCollections.observableArrayList();

    private UserFilterDTO filterUser = new UserFilterDTO();
    private FriendshipFilterDTO filterFriendship = new FriendshipFilterDTO();

    //User window
    @FXML
    private TableView<User> userTableView;
    @FXML
    private TableColumn<User, Long> idUser;
    @FXML
    private TableColumn<User, String> firstName;
    @FXML
    private TableColumn<User, String> lastName;
    @FXML
    private TableColumn<User, String> emailUser;
    @FXML
    private TextField textFirstName;
    @FXML
    private TextField textLastName;
    @FXML
    private TextField textEmail;
    @FXML
    private TextField textIDUpdateUser;
    @FXML
    private TextField textIDSearchUser;
    @FXML
    private Label pageNumber;
    @FXML
    private TextField textPageSize;
    private int currentPage = 0;
    private int pageSize;
    private int totalNumberOfElements = 0;
    @FXML
    private Button nextButton;
    @FXML
    private Button previousButton;

    // Friendships window
    @FXML
    private TableView<Friendship> friendshipTableView;
    @FXML
    private TableColumn<Friendship, Long> idFriendship;
    @FXML
    private TableColumn<Friendship, Long> idUser1;
    @FXML
    private TableColumn<Friendship, Long> idUser2;
    @FXML
    private TableColumn<Friendship, LocalDateTime> friendsFrom;
    @FXML
    private TableColumn<Friendship, FriendRequest> friendshipStatus;
    @FXML
    private TextField textEmail1;
    @FXML
    private TextField textEmail2;
    @FXML
    private Label pageNumberF;
    @FXML
    private TextField textPageSizeF;
    private int currentPageF = 0;
    private int pageSizeF;
    private int totalNumberOfElementsF = 0;
    @FXML
    private Button nextButtonF;
    @FXML
    private Button previousButtonF;

    // Messages window
    @FXML
    private ListView<Message> messagesListView;
    @FXML
    private TextField sendEmailFrom;
    @FXML
    private TextField sendEmailTo;
    @FXML
    private TextField message;
    @FXML
    private TextField searchMessageEmail1;
    @FXML
    private TextField searchMessageEmail2;

    private ActionEvent actionEvent;

    public void setService(Service srv) {
        this.srv = srv;
    }

    public void initialize() {
        userTableView.setItems(usersObs);

        idUser.setCellValueFactory(new PropertyValueFactory<>("id"));
        firstName.setCellValueFactory(new PropertyValueFactory<>("firstName"));
        lastName.setCellValueFactory(new PropertyValueFactory<>("lastName"));
        emailUser.setCellValueFactory(new PropertyValueFactory<>("email"));

        friendshipTableView.setItems(friendshipsObs);

        idFriendship.setCellValueFactory(new PropertyValueFactory<>("id"));
        idUser1.setCellValueFactory(new PropertyValueFactory<>("user1_id"));
        idUser2.setCellValueFactory(new PropertyValueFactory<>("user2_id"));
        friendsFrom.setCellValueFactory(new PropertyValueFactory<>("friendsFrom"));
        friendshipStatus.setCellValueFactory(new PropertyValueFactory<>("friendRequestStatus"));
    }

    private void initModel() {
        if(!Objects.equals(textPageSize.getText(), "")) {
            pageSize = Integer.parseInt(textPageSize.getText());
        } else {
            pageSize = 7;
        }

        Page<User> page = srv.findAll(new Pageable(currentPage, pageSize),filterUser);

        int maxPage = (int) Math.ceil((double) page.getTotalElementCount() / pageSize ) - 1;
        if(maxPage == -1)
        {
            maxPage = 0;
        }
        if(currentPage > maxPage) {
            currentPage = maxPage;
            page = srv.findAll(new Pageable(currentPage, pageSize),filterUser);
        }

        usersObs.setAll(StreamSupport.stream(page.getElementsOnPage().spliterator(),
                false).collect(Collectors.toList()));
        totalNumberOfElements = page.getTotalElementCount();

        previousButton.setDisable(currentPage == 0);
        nextButton.setDisable((currentPage + 1) * pageSize >= totalNumberOfElements);

        pageNumber.setText("Page "+(currentPage+1)+"/"+(maxPage+1));
    }

    private void initModelFriendship() {
        if(!Objects.equals(textPageSizeF.getText(), "")) {
            pageSizeF = Integer.parseInt(textPageSizeF.getText());
        } else {
            pageSizeF = 5;
        }

        Page<Friendship> page = srv.findAll(new Pageable(currentPageF, pageSizeF),filterFriendship);

        int maxPage = (int) Math.ceil((double) page.getTotalElementCount() / pageSizeF ) - 1;
        if(maxPage == -1)
        {
            maxPage = 0;
        }
        if(currentPageF > maxPage) {
            currentPageF = maxPage;
            page = srv.findAll(new Pageable(currentPageF, pageSizeF),filterFriendship);
        }

        friendshipsObs.setAll(StreamSupport.stream(page.getElementsOnPage().spliterator(),
                false).collect(Collectors.toList()));
        totalNumberOfElementsF = page.getTotalElementCount();

        previousButtonF.setDisable(currentPageF == 0);
        nextButtonF.setDisable((currentPageF + 1) * pageSizeF >= totalNumberOfElementsF);

        pageNumberF.setText("Page "+(currentPageF+1)+"/"+(maxPage+1));
    }

    public void initApp() {
        initModel();
        initModelFriendship();
        //usersObs.setAll(StreamSupport.stream(srv.getAllUsers().spliterator(), false).collect(Collectors.toList()));
        //friendshipsObs.setAll(StreamSupport.stream(srv.getAllFriendships().spliterator(), false).collect(Collectors.toList()));
    }

    private void clearTextFieldsUsers() {
        textFirstName.clear();
        textLastName.clear();
        textEmail.clear();

        textIDUpdateUser.clear();
        textIDSearchUser.clear();
    }

    private void clearTextFieldsFriendships() {
        textEmail1.clear();
        textEmail2.clear();
    }

    @FXML
    public void onPressAddUser(ActionEvent actionEvent) {
        Repository<Long, User> userRepo = srv.getUserRepo();

        this.actionEvent = actionEvent;
        try{
            String first_name = textFirstName.getText();
            String last_name = textLastName.getText();
            String email = textEmail.getText();

            User newUser = new User(first_name, last_name, email);
            userRepo.save(newUser);

            initModel();
            clearTextFieldsUsers();
        } catch (Exception e) {
            MessageAlert.showErrorMessage(null, e.getMessage());
        }
    }

    @FXML
    public void onPressUpdateUser(ActionEvent actionEvent) {
        Repository<Long, User> userRepo = srv.getUserRepo();

        try{
            Long id = Long.valueOf(textIDUpdateUser.getText());
            String first_name = textFirstName.getText();
            String last_name = textLastName.getText();
            String email = textEmail.getText();

            User selectedUser = userRepo.findOne(id);
            if(selectedUser != null) {
                boolean hasUpdates = false;

                if(!first_name.isEmpty()) {
                    selectedUser.setFirstName(first_name);
                    hasUpdates = true;
                }
                if(!last_name.isEmpty()) {
                    selectedUser.setLastName(last_name);
                    hasUpdates = true;
                }
                if(!email.isEmpty()) {
                    selectedUser.setEmail(email);
                    hasUpdates = true;
                }

                if(hasUpdates) {
                    userRepo.update(selectedUser);
                    initModel();
                    clearTextFieldsUsers();
                } else {
                    MessageAlert.showErrorMessage(null, "No update provided");
                }

            } else {
                MessageAlert.showErrorMessage(null, "User not found");
            }
        } catch (Exception e) {
            MessageAlert.showErrorMessage(null, e.getMessage());
        }
    }

    @FXML
    public void onPressDeleteUser(ActionEvent actionEvent) {
        Repository<Long, User> userRepo = srv.getUserRepo();

        User selectedUser = userTableView.getSelectionModel().getSelectedItem();
        if(selectedUser != null) {
            userRepo.delete(selectedUser.getId());
            initModel();
        } else {
            MessageAlert.showErrorMessage(null, "No user selected");
        }
    }

    @FXML
    public void onPressSearchUser(ActionEvent actionEvent) {
        Repository<Long, User> userRepo = srv.getUserRepo();

        try{
            Long id = Long.valueOf(textIDSearchUser.getText());

            User searchUser = userRepo.findOne(id);
            if(searchUser != null) {
                usersObs.clear();
                usersObs.add(searchUser);

                previousButton.setDisable(true);
                nextButton.setDisable(true);
                pageNumber.setText("Page 1/1");

                clearTextFieldsUsers();
            } else {
                MessageAlert.showErrorMessage(null, "User not found");
            }
        } catch (Exception e) {
            MessageAlert.showErrorMessage(null, e.getMessage());
        }
    }

    @FXML
    public void onPressReloadUsers(ActionEvent actionEvent) {
        initModel();
        clearTextFieldsUsers();
    }

    @FXML
    public void onPrevious(ActionEvent actionEvent) {
        currentPage--;
        initModel();
    }

    @FXML
    public void onNext(ActionEvent actionEvent) {
        currentPage++;
        initModel();
    }

    @FXML
    public void onPagination(ActionEvent actionEvent) {
        //int pageSize = Integer.valueOf(textPageSize.getText());
        initModel();
    }

    @FXML
    public void onPressAddFriendship(ActionEvent actionEvent) {
        this.actionEvent = actionEvent;
        try{
            String email1 = textEmail1.getText();
            String email2 = textEmail2.getText();

            if(!srv.createFriendRequest(email1, email2))
                throw new Exception("Something went wrong");

            initModelFriendship();
            clearTextFieldsFriendships();
        } catch (Exception e) {
            MessageAlert.showErrorMessage(null, e.getMessage());
        }
    }

    @FXML
    public void onPressDeleteFriendship(ActionEvent actionEvent) {
        Repository<Long, Friendship> friendshipRepo = srv.getFriendshipRepo();

        try {
            Friendship selectedFriendship = friendshipTableView.getSelectionModel().getSelectedItem();
            if (selectedFriendship != null) {
                friendshipRepo.delete(selectedFriendship.getId());
                initModelFriendship();
            } else {
                MessageAlert.showErrorMessage(null, "No friendship selected");
            }
        } catch (Exception e) {
            MessageAlert.showErrorMessage(null, e.getMessage());
        }
    }

    @FXML
    public void onPressAcceptFriendsReq(ActionEvent actionEvent) {
        Friendship selectedFriendship = friendshipTableView.getSelectionModel().getSelectedItem();
        if(selectedFriendship != null) {
            srv.respondFriendRequest(selectedFriendship, FriendRequest.ACCEPTED);
            initModelFriendship();
        } else {
            MessageAlert.showErrorMessage(null, "No friendship selected");
        }
    }

    @FXML
    public void onPressRejectFriendReq(ActionEvent actionEvent) {
        Friendship selectedFriendship = friendshipTableView.getSelectionModel().getSelectedItem();
        if(selectedFriendship != null) {
            srv.respondFriendRequest(selectedFriendship, FriendRequest.REJECTED);
            initModelFriendship();
        } else {
            MessageAlert.showErrorMessage(null, "No friendship selected");
        }
    }

    @FXML
    public void onPressReloadFriendships(ActionEvent actionEvent) {
        initModelFriendship();
        clearTextFieldsFriendships();
    }

    @FXML
    public void onPreviousF(ActionEvent actionEvent) {
        currentPageF--;
        initModelFriendship();
    }

    @FXML
    public void onNextF(ActionEvent actionEvent) {
        currentPageF++;
        initModelFriendship();
    }

    @FXML
    public void onPaginationF(ActionEvent actionEvent) {
        //int pageSizeFriendship = Integer.parseInt(textPageSizeF.getText());
        initModelFriendship();
    }

    @FXML
    public void onPressAcceptedFriends(ActionEvent actionEvent) {
        filterFriendshipsByStatus(FriendRequest.ACCEPTED);

        previousButtonF.setDisable(true);
        nextButtonF.setDisable(true);
        pageNumberF.setText("Page 1/1");
    }

    @FXML
    public void onPressRejectedFriends(ActionEvent actionEvent) {
        filterFriendshipsByStatus(FriendRequest.REJECTED);

        previousButtonF.setDisable(true);
        nextButtonF.setDisable(true);
        pageNumberF.setText("Page 1/1");
    }

    @FXML
    public void onPressPendingFriends(ActionEvent actionEvent) {
        filterFriendshipsByStatus(FriendRequest.PENDING);

        previousButtonF.setDisable(true);
        nextButtonF.setDisable(true);
        pageNumberF.setText("Page 1/1");
    }

    private void filterFriendshipsByStatus(FriendRequest status) {
        friendshipsObs.clear(); // Clear current list to display filtered friendships

        for (Friendship friendship : srv.getAllFriendships()) {
            if (friendship.getFriendRequestStatus() == status) {
                friendshipsObs.add(friendship);
            }
        }
    }

    public void loadListOfMessages(String emailFrom, String emailTo) {
        messagesListView.getItems().clear();
        messagesObs.clear();

        for(Message msg : srv.getMessagesBetweenTwoUsers(emailFrom, emailTo)) {
            messagesObs.add(msg);
        }
        if(messagesObs.isEmpty()) {
            MessageAlert.showErrorMessage(null, "Mo messages");
        }

        messagesListView.setItems(messagesObs);
    }

    @FXML
    public void onPressSend(ActionEvent actionEvent) {
        String emailFrom = sendEmailFrom.getText();
        String emailTo = sendEmailTo.getText();
        List<String> toUsers = new ArrayList<>(Arrays.asList(emailTo.split(" ")));
        String msg = message.getText();

        if(!srv.addMessage(emailFrom, toUsers, msg)) {
            MessageAlert.showErrorMessage(null, "Something wrong");
        } else {
            loadListOfMessages(emailFrom, toUsers.get(0));
        }

        message.clear();
    }

    @FXML
    public void onPressReply(ActionEvent actionEvent) {
        if(messagesListView.getSelectionModel().getSelectedItem() != null) {
            Message msg = messagesListView.getSelectionModel().getSelectedItem();

            String emailFrom = sendEmailFrom.getText();
            String emailTo = sendEmailTo.getText();
            sendEmailFrom.setText(emailTo);
            sendEmailTo.setText(emailFrom);

            List<String> toUsers = new ArrayList<>(Arrays.asList(emailTo.split(" ")));
            String replyText = message.getText();

            if(!srv.addMessage(emailFrom, toUsers, replyText, msg)) {
                MessageAlert.showErrorMessage(null, "Something wrong");
            } else {
                loadListOfMessages(emailFrom, toUsers.get(0));
            }

            message.clear();
        }
    }

    @FXML
    public void onPressSearchMessage(ActionEvent actionEvent) {
        String email1 = searchMessageEmail1.getText();
        String email2 = searchMessageEmail2.getText();

        searchMessageEmail1.clear();
        searchMessageEmail2.clear();

        sendEmailFrom.setText(email1);
        sendEmailTo.setText(email2);

        loadListOfMessages(email1, email2);
    }
}
