const today = new Date();
const year = today.getFullYear();
const day = today.getDate();
const month = today.getMonth() + 1;

// 🎂 CHANGE HERE
const BDAY_DAY = 12;
const BDAY_MONTH = 7;

const isBirthday = (day === BDAY_DAY && month === BDAY_MONTH);

// Birthday page logic
if (isBirthday && window.location.pathname.includes("index.html")) {
  window.location.href = "birthday.html";
}

// Button → yearly letter
const btn = document.getElementById("enterBtn");
if (btn) {
  btn.onclick = () => {
    window.location.href = "letters/" + year + ".html";
  };
}
