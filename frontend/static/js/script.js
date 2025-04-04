
//---------------------------------------------------------------------------------

// Chatbot Toggle Functionality

function toggleChat() {
    let chatContainer = document.getElementById("chat-container");
    chatContainer.style.display = chatContainer.style.display === "none" ? "block" : "none";
}

function sendMessage() {
    let userInput = document.getElementById("chat-input").value;
    let chatBox = document.getElementById("chat-box");
    
    if (userInput.trim() === "") return;
    
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    document.getElementById("chat-input").value = "";
    
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}

//---------------------------------------------------------------------------------