const EMAILJS_SERVICE_ID = "gyeonggi.gajogae-waste";
const EMAILJS_TEMPLATE_ID = "template_wwbariw";
const EMAILJS_PUBLIC_KEY = "JKsVOKPtnWHIr2BCV";

(function () {
  const script = document.createElement("script");
  script.src = "https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js";
  script.onload = function () {
    emailjs.init(EMAILJS_PUBLIC_KEY);
  };
  document.head.appendChild(script);
})();

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("#contactForm").forEach(function (form) {
    const messageBox = form.querySelector("#formMessage") || document.getElementById("formMessage");

    form.addEventListener("submit", function (event) {
      event.preventDefault();

      if (messageBox) {
        messageBox.textContent = "접수 중입니다. 잠시만 기다려주세요.";
      }
      const fullMessage =
        "[경기 가족애폐기물처리 상담접수]\n\n" +
        "성함: " + (form.name?.value || "") + "\n" +
        "연락처: " + (form.phone?.value || "") + "\n" +
        "작업지역: " + (form.region?.value || "") + "\n" +
        "필요 서비스: " + (form.service?.value || "") + "\n\n" +
        "문의내용:\n" +
        (form.message?.value || "내용 없음") + "\n\n" +
        "접수 페이지:\n" +
        window.location.href;

      const data = {
        title: "[경기 가족애폐기물처리] 상담접수",
        name: fullMessage,
        message: fullMessage
};

      emailjs
        .send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, data)
        .then(function () {
          if (messageBox) {
            messageBox.textContent =
              "접수가 완료되었습니다. 담당자가 확인 후 연락드리겠습니다.";
          }
          form.reset();
        })
        
        .catch(function (error) {
          console.error("EmailJS 전체 오류:", JSON.stringify(error));
          console.error(error);
          if (messageBox) {
            messageBox.textContent =
              "접수 중 오류가 발생했습니다. 전화상담 010-4720-3895로 연락주세요.";
          }
        });
    });
  });
});