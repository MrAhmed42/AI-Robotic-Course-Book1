import React, { useState, useEffect } from 'react';
import styles from './ChatbotWidget.module.css';

const ChatbotWidget = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState([]);
    const [inputValue, setInputValue] = useState('');
    const [selectedText, setSelectedText] = useState('');
    // 1. ADD LOADING STATE
    const [isLoading, setIsLoading] = useState(false); 

    const toggleChat = () => {
        setIsOpen(!isOpen);
    };

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    };

    const handleSend = async () => {
        if (inputValue.trim() === '' || isLoading) return; // Prevent multiple sends while loading

        const userQuestion = inputValue;
        const userMessage = { text: userQuestion, sender: 'user' };
        
        // 2. SET LOADING STATE AND ADD USER MESSAGE
        setIsLoading(true);
        setMessages(prevMessages => [...prevMessages, userMessage]); 
        setInputValue(''); // Clear input box

        try {
            // Note: Using port 8080 as per our last successful Uvicorn startup
            const response = await fetch('http://127.0.0.1:8000/api/chat/query', { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question: userQuestion, selected_text: selectedText }),
            });
            
            // Handle HTTP errors (e.g., 404, 500)
            if (!response.ok) {
                const errorData = await response.json();
                const detail = errorData.detail || `HTTP Error ${response.status}: Failed to get a proper response.`;
                throw new Error(detail);
            }

            const data = await response.json();
            
            // 3. Extract the bot message using the correct key 'message'
            const botResponseText = data.message || "Error: AI response text was empty (key 'message' was empty).";

            const botMessage = { text: botResponseText, sender: 'bot' };
            
            // 4. Add the bot message using the functional update form
            setMessages(prevMessages => [...prevMessages, botMessage]);
            
            setSelectedText('');

        } catch (error) {
            console.error("API Fetch/Process Error:", error);
            
            // Display the detailed error message in the chat window
            const errorMessage = { 
                text: `CRITICAL ERROR: ${error.message}. Please check browser console and Uvicorn terminal.`, 
                sender: 'bot' 
            };
            
            // Add error message to the chat
            setMessages(prevMessages => [...prevMessages, errorMessage]);
        } finally {
            // 5. CLEAR LOADING STATE
            setIsLoading(false);
        }
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
                Ask AI
            </button>
            {isOpen && (
                <div className={styles.chatWindow}>
                    <div className={styles.messages}>
                        {messages.map((message, index) => (
                            <div key={index} className={`${styles.message} ${styles[message.sender]}`}>
                                {message.text}
                            </div>
                        ))}
                        {/* 6. SHOW LOADING INDICATOR */}
                        {isLoading && (
                            <div className={`${styles.message} ${styles.bot} ${styles.loading}`}>
                                Thinking...
                            </div>
                        )}
                    </div>
                    {selectedText && <div className={styles.selectedText}>Selected text: {selectedText}</div>}
                    <div className={styles.inputArea}>
                        <input
                            type="text"
                            value={inputValue}
                            onChange={handleInputChange}
                            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                            disabled={isLoading} // Correct JSX syntax
                        />
                        {/* Ensure the button also uses correct JSX syntax */}
                        <button onClick={handleSend} disabled={isLoading}>Ask</button> 
                    </div>
                </div>
            )}
        </div>
    );
};

export default ChatbotWidget;