package com.ammasdoughy.backend.service;

import com.ammasdoughy.backend.model.ContactMessage;
import com.ammasdoughy.backend.repository.ContactRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ContactService {

    @Autowired
    private ContactRepository contactRepository;

    public ContactMessage saveContactMessage(ContactMessage contactMessage) {
        return contactRepository.save(contactMessage);
    }
}
