// Sends the contact form without leaving the page. Without JavaScript the form still posts
// normally and the studio sends the visitor to /thanks or /inquiry-problem.
(function () {
  var form = document.querySelector("form[data-inquiry]");
  if (!form || !window.fetch || !window.FormData) return;
  var status = form.querySelector("[data-status]");
  var button = form.querySelector('button[type="submit"]');
  var label = button.innerHTML;
  function say(text, tone) {
    status.textContent = text;
    status.setAttribute("data-tone", tone);
  }
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    button.disabled = true;
    button.textContent = "Sending…";
    say("", "");
    fetch(form.action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
      .then(function (res) {
        if (res.ok) {
          form.reset();
          say("Thanks, your message is on its way. We reply within one business day.", "ok");
        } else if (res.status === 429) {
          say("Several messages were just sent from here. Please wait a while, or call or text (470) 632-6701.", "error");
        } else if (res.status === 400) {
          say("Please check the form: name, a valid email and a message are needed.", "error");
        } else {
          say("Your message couldn't be sent. Please call or text (470) 632-6701.", "error");
        }
      })
      .catch(function () {
        say("Your message couldn't be sent. Please call or text (470) 632-6701.", "error");
      })
      .then(function () {
        button.disabled = false;
        button.innerHTML = label;
      });
  });
})();
