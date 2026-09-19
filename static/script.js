const sendButton = document.getElementById("send-button");


async function sendMessage() {
    const welcome_banner = document.querySelector(".welcome-banner");
    const input = document.getElementById("input");
    const messages = document.querySelector(".messages");
    const message = input.value;

    if (!message) return;

    if (welcome_banner) {
        welcome_banner.remove();
    }

    // User message
    const userMessage = document.createElement("div");
    userMessage.className = "message user";
    userMessage.textContent = message;
    messages.appendChild(userMessage);

    input.value = "";

    messages.scrollTop = messages.scrollHeight;

    // Thinking message
    const thinking = document.createElement("div");
    thinking.className = "message cat thinking";
    thinking.textContent = "Coco is thinking...";
    messages.appendChild(thinking);


    messages.scrollTop = messages.scrollHeight;

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    const data = await response.json();

    // Remove thinking message
    thinking.remove();

    // Coco message
    const catMessage = document.createElement("div");
    catMessage.className = "message cat";
    catMessage.textContent = data.response;
    messages.appendChild(catMessage);

    messages.scrollTop = messages.scrollHeight;

}


document.getElementById("input").addEventListener("keydown", (event) => {
    if (event.key === "Enter") sendMessage();
});

sendButton.addEventListener("click", sendMessage);