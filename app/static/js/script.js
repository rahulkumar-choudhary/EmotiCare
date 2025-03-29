async function sendMessage() {
    const userMessage = document.getElementById("userMessage").value;
    const response = await fetch("/chatbot/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
    });
    
    const data = await response.json();
    document.getElementById("chatResponse").innerText = data.response || "Error getting response";
}
