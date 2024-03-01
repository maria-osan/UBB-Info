package com.example.lab10_2.domain.validators;

import com.example.lab10_2.domain.Friendship;

public class FriendshipValidator implements Validator<Friendship> {
    @Override
    public void validate(Friendship entity) throws ValidationException {
        if(entity.getUser1_id() == entity.getUser2_id())
            throw new ValidationException("Error - you cant add yourself as a friend!");
    }
}
