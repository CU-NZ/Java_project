package com.item.chatroom.dao;

import com.item.chatroom.entity.User;
import org.junit.Assert;
import org.junit.Test;

/**
 * @author: ChangYajie
 * @date: 2019/8/5
 */
public class AccountDaoTest {

        private AccountDao accountDao = new AccountDao();
        @Test
        public void userLogin() {
            User user = accountDao.userLogin("test","123");
            System.out.println(user);
            Assert.assertNotNull(user);
        }

        @Test
        public void userRegister() {
            User user = new User();
            user.setUserName("test2");
            user.setPassword("123");
            boolean isSuccess = accountDao.userRegister(user);
            Assert.assertEquals(true,isSuccess);
    }
}