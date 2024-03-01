package com.example.lab10_2.domain.validators;

public interface Validator<T> {
    void validate(T entity) throws ValidationException;
}
