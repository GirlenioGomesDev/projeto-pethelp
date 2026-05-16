document.addEventListener('DOMContentLoaded', () => {
  const counters = document.querySelectorAll('.stat-number');

  counters.forEach((counter) => {
    const target = Number(counter.dataset.count || 0);
    const duration = 900;
    const start = performance.now();

    const tick = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      counter.textContent = Math.round(target * eased);

      if (progress < 1) {
        requestAnimationFrame(tick);
      }
    };

    requestAnimationFrame(tick);
  });

  document.querySelectorAll('form').forEach((form) => {
    form.addEventListener('submit', () => {
      form.classList.add('is-loading');
    });
  });
});
