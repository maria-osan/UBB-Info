package cinema.domain.validators;

import cinema.domain.User;

public class UserValidator implements Validator<User> {
    @Override
    public void validate(User entity) throws ValidationException {
        validateName(entity.getName());
        validateEmail(entity.getEmail());
        validateUsername(entity.getUsername());
        validatePassword(entity.getPassword());
    }

    private void validateName(String name) throws ValidationException {
        if(name == null)
            throw new ValidationException("Invalid name - it is null!");
        else if(name.isEmpty())
            throw new ValidationException("Invalid name - it is empty!");
        else if(! name.matches("[a-zA-Z]+"))
            throw new ValidationException("Invalid name - must contain only letters!");
    }

    private void validateEmail(String email) throws ValidationException {
        if(email == null)
            throw new ValidationException("Invalid email - it is null!");
        else if(email.isEmpty())
            throw new ValidationException("Invalid email - it is empty!");
        else if(! email.matches("[a-zA-Z]+[a-zA-Z0-9._]*@[a-z]+.[a-z]+"))
            throw new ValidationException("Invalid email address!");
    }

    private void validateUsername(String username) throws ValidationException {
        if(username == null)
            throw new ValidationException("Invalid username - it is null!");
        else if(username.isEmpty())
            throw new ValidationException("Invalid username - it is empty!");
        else if(!username.matches("[a-zA-Z]+[0-9_.-]*"))
            throw new ValidationException("Invalid username!");
    }

    private void validatePassword(String password) throws ValidationException {
        if(password == null)
            throw new ValidationException("Invalid password - it is null!");
        else if(password.isEmpty())
            throw new ValidationException("Invalid password - it is empty!");
        else if(!password.matches("[a-zA-Z0-9!@#$%^&*_+?;',.]+"))
            throw new ValidationException("Invalid password!");
    }
}
