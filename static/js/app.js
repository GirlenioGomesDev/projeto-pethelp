document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.querySelector('input[type="file"][name="foto"]');
  const preview = document.querySelector('#image-preview');
  const placeholder = document.querySelector('#preview-placeholder');

  if (preview && preview.getAttribute('src')) {
    preview.style.display = 'block';
    if (placeholder) placeholder.style.display = 'none';
  }

  if (fileInput && preview) {
    fileInput.addEventListener('change', () => {
      const [file] = fileInput.files;
      if (!file) return;

      preview.src = URL.createObjectURL(file);
      preview.style.display = 'block';
      if (placeholder) placeholder.style.display = 'none';
    });
  }

  document.querySelectorAll('.message').forEach((message) => {
    setTimeout(() => {
      message.style.opacity = '0';
      message.style.transform = 'translateY(-6px)';
    }, 4800);
  });
});
