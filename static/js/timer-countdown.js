// function startTimer() {
//   const countdownElement = document.getElementById('countdown');
//   let timeLeft = 120; // 2 دقیقه = 120 ثانیه
//
//   // بررسی مقدار ذخیره شده در Local Storage
//   const storedTime = localStorage.getItem('timeLeft');
//   if (storedTime) {
//     timeLeft = parseInt(storedTime);
//   }
//
//   const intervalId = setInterval(() => {
//     timeLeft--;
//
//     // فرمت دهی زمان به صورت دقیقه:ثانیه
//     const minutes = Math.floor(timeLeft / 60);
//     const seconds = timeLeft % 60;
//     countdownElement.textContent = `${minutes}:${seconds.toString().padStart(2,  
//  '0')}`;
//
//     // ذخیره زمان باقی‌مانده در Local Storage
//     localStorage.setItem('timeLeft', timeLeft);
//
//     if (timeLeft === 0) {
//       clearInterval(intervalId);
//       // انجام عملیات پس از اتمام زمان (مثلاً نمایش پیام خطا)
//       alert('زمان شما به پایان رسید.');
//       localStorage.removeItem('timeLeft'); // پاک کردن Local Storage
//     }
//   }, 1000);
//   window.addEventListener('beforeunload', () => {
//     localStorage.removeItem('timeLeft');
//     localStorage.clear()
//   });
// }
//
// // شروع تایمر
// startTimer();


function startTimer() {
  const countdownElement = document.getElementById('countdown');
  let timeLeft = 120; // 2 دقیقه = 120 ثانیه

  const intervalId = setInterval(() => {
    timeLeft--;

    // فرمت دهی زمان به صورت دقیقه:ثانیه
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    countdownElement.textContent = `${minutes}:${seconds.toString().padStart(2,   
 '0')}`;

    if (timeLeft === 0) {
      clearInterval(intervalId);
      // انجام عملیات پس از اتمام زمان (مثلاً نمایش پیام خطا)
      alert('زمان شما به پایان رسید.');
    }
  }, 1000);
}

// شروع تایمر
startTimer();


