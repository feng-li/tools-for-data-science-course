{
  "cells": [
   {
    "cell_type": "code",
    "execution_count": 1,
    "metadata": {},
    "outputs": [],
    "source": [
     "from selenium import webdriver\n",
     "import time  \n",
     "driver = webdriver.Firefox()"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 2,
    "metadata": {},
    "outputs": [],
    "source": [
     "driver.get(\"https://mail.qq.com\")"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 3,
    "metadata": {},
    "outputs": [],
    "source": [
     "driver.find_element_by_id('switchAccountLogin').click()"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 4,
    "metadata": {},
    "outputs": [],
    "source": [
     "iframe = driver.find_element_by_xpath('//div[@id=\"loginDiv\"]/iframe')\n",
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 5,
    "metadata": {},
    "outputs": [],
    "source": [
     "driver.switch_to.frame(iframe)"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 6,
    "metadata": {},
    "outputs": [],
    "source": [
     "email_input = driver.find_element_by_name(\"email\")"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 7,
    "metadata": {},
    "outputs": [],
    "source": [
     "email_input.clear()"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 8,
    "metadata": {},
    "outputs": [],
    "source": [
     "email_input.send_keys(\"’À∫≈\")"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 9,
    "metadata": {},
    "outputs": [],
    "source": [
     "password_input = driver.find_element_by_name(\"password\")"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 10,
    "metadata": {},
    "outputs": [],
    "source": [
     "password_input.send_keys(\"√‹¬Î\")"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 11,
    "metadata": {},
    "outputs": [],
    "source": [
     "driver.find_element_by_id('dologin').click() "
    ]
   }
  ],
  "metadata": {
   "kernelspec": {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
   },
   "language_info": {
    "codemirror_mode": {
     "name": "ipython",
     "version": 3
    },
    "file_extension": ".py",
    "mimetype": "text/x-python",
    "name": "python",
    "nbconvert_exporter": "python",
    "pygments_lexer": "ipython3",
    "version": "3.7.4"
   }
  },
  "nbformat": 4,
  "nbformat_minor": 2
 }