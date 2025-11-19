document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const chatInput = document.getElementById("chat-input");
    const chatSend = document.getElementById("chat-send");

    function addMessage(sender, text) {
        chatBox.value += `${sender}: ${text}\n`;
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function postJSON(url, data) {
        const res = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });
        return res.json();
    }

    // CHAT SEND
    chatSend.addEventListener("click", async () => {
        const userText = chatInput.value.trim();
        if (!userText) return;

        addMessage("You", userText);
        chatInput.value = "";

        let response = await postJSON("/agent", { prompt: userText });

        if (response.reply) {
            addMessage("AI", response.reply);
        } else {
            addMessage("AI", "Error: " + JSON.stringify(response));
        }
    });

    // MEAL PLAN
    document.getElementById("plan-btn").addEventListener("click", async () => {
        const foods = document.getElementById("foods-input").value.trim();
        const res = await postJSON("/meal-plan", { foods });

        document.getElementById("plan-result").innerText = res.plan || "No response.";
    });

    // RESEARCH
    document.getElementById("research-btn").addEventListener("click", async () => {
        const q = document.getElementById("research-query").value.trim();
        const res = await postJSON("/research", { query: q });

        document.getElementById("research-results").innerText =
            res.results || "No results.";
    });

    // CALORIE CHART
    document.getElementById("chart-btn").addEventListener("click", async () => {
        const foods = document.getElementById("foods-input").value.trim();
        document.getElementById("chart-img").src = "/calories-chart?foods=" + encodeURIComponent(foods);
        document.getElementById("chart-img").style.display = "block";
    });
});
