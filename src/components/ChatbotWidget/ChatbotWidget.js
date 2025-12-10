import React, { useState, useEffect } from 'react';
import styles from './ChatbotWidget.module.css';

const ChatbotWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [selectedText, setSelectedText] = useState('');

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSend = async () => {
    if (inputValue.trim() === '') return;

    const newMessages = [...messages, { text: inputValue, sender: 'user' }];
    setMessages(newMessages);
    setInputValue('');

    const response = await fetch('http://127.0.0.1:8000/api/chat/query', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question: inputValue, selected_text: selectedText }),
    });

    const data = await response.json();
    const botMessage = { text: data.message, sender: 'bot' };
    setMessages([...newMessages, botMessage]);
    setSelectedText('');
  };
  
  const handleTextSelection = () => {
    const selection = window.getSelection().toString();
    if (selection) {
      setSelectedText(selection);
    }
  };

  useEffect(() => {
    document.addEventListener('selectionchange', handleTextSelection);
    return () => {
      document.removeEventListener('selectionchange', handleTextSelection);
    };
  }, []);


  return (
    <div className={styles.chatbotWidget}>
      <button className={styles.chatButton} onClick={toggleChat}>
        Chat
      </button>
      {isOpen && (
        <div className={styles.chatWindow}>
          <div className={styles.messages}>
            {messages.map((message, index) => (
              <div key={index} className={`${styles.message} ${styles[message.sender]}`}>
                {message.text}
              </div>
            ))}
          </div>
          {selectedText && <div className={styles.selectedText}>Selected text: {selectedText}</div>}
          <div className={styles.inputArea}>
            <input
              type="text"
              value={inputValue}
              onChange={handleInputChange}
              onKeyPress={(e) => e.key === 'Enter' && handleSend()}
            />
            <button onClick={handleSend}>Send</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatbotWidget;
