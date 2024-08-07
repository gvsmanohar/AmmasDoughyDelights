package com.ammasdoughy.backend.controller;

import com.ammasdoughy.backend.model.ContactMessage;
import com.ammasdoughy.backend.service.ContactService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@RestController
@RequestMapping("/api/contact")
public class ContactController {

    private static final Logger logger = LoggerFactory.getLogger(ContactController.class);

    @Autowired
    private ContactService contactService;

    @PostMapping
    public ContactMessage createContactMessage(@RequestBody ContactMessage contactMessage) {
        logger.info("Received contact message: {}", contactMessage);
        return contactService.saveContactMessage(contactMessage);
    }
}
