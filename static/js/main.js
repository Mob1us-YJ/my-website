document.addEventListener('DOMContentLoaded', function() {
    // 简单的交互效果
    const navLinks = document.querySelectorAll('nav a');

    navLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });

        link.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // 控制台欢迎信息
    console.log('Welcome to my personal website!');
});