// main.js
document.addEventListener('DOMContentLoaded', function() {
    const ticketForm = document.getElementById('ticket-form');

    ticketForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const username = document.getElementById('username').value;
        const message = document.getElementById('message').value;

        // 서버로 데이터 전송
        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `username=${encodeURIComponent(username)}&message=${encodeURIComponent(message)}`,
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            console.log(data); // 성공한 경우에는 서버에서 'Success'를 반환
            alert('문의가 성공적으로 제출되었습니다.');
            ticketForm.reset(); // 폼 비우기
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
            alert('문의 제출 중 오류가 발생했습니다.');
        });
    });
});
