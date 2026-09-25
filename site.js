// All reading, navigation, and external links work without JavaScript.
document.querySelectorAll('[data-year]').forEach(node => { node.textContent = String(new Date().getFullYear()); });

document.querySelectorAll('[data-video]').forEach(button => {
  const video = document.getElementById(button.dataset.video);
  if (!video) return;
  const idleMarkup = button.innerHTML;
  const idleLabel = button.getAttribute('aria-label');
  const reset = () => { button.innerHTML = idleMarkup; button.setAttribute('aria-pressed', 'false'); button.setAttribute('aria-label', idleLabel); };
  const playing = () => { button.innerHTML = '<span aria-hidden="true">Ⅱ</span> Pause'; button.setAttribute('aria-pressed', 'true'); button.setAttribute('aria-label', 'Pause video'); };
  button.addEventListener('click', async () => {
    if (!video.paused) { video.pause(); return; }
    try { await video.play(); } catch { video.controls = true; button.hidden = true; }
  });
  video.addEventListener('play', playing);
  video.addEventListener('pause', reset);
  video.addEventListener('ended', reset);
  // Stop offscreen playback; media starts only when the visitor chooses to play.
  if ('IntersectionObserver' in window) new IntersectionObserver(entries => {
    if (!entries[0].isIntersecting) video.pause();
  }, { threshold: 0.05 }).observe(video);
});

document.querySelectorAll('[data-copy]').forEach(button => {
  button.addEventListener('click', async () => {
    const status = button.parentElement.querySelector('[role="status"]');
    try {
      if (!navigator.clipboard) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(button.dataset.copy);
      status.textContent = 'Email copied';
    } catch {
      status.textContent = 'Select the email above to copy it, or click to email me.';
    }
  });
});

// Keep a normal YouTube link when scripting is off, and load the embedded
// player only after a visitor chooses to watch the external demonstration.
document.querySelectorAll('[data-youtube]').forEach(link => {
  link.addEventListener('click', event => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const id = link.dataset.youtube;
    if (!/^[a-zA-Z0-9_-]{11}$/.test(id)) return;
    event.preventDefault();
    const frame = document.createElement('iframe');
    frame.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0`;
    frame.title = link.dataset.videoTitle;
    frame.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
    frame.allowFullscreen = true;
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    link.replaceWith(frame);
    frame.focus();
  });
});

if ('IntersectionObserver' in window) {
  const links = [...document.querySelectorAll('nav a[href^="#"]')];
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      const link = links.find(item => item.hash === '#' + entry.target.id);
      if (!link) return;
      if (entry.isIntersecting) { links.forEach(item => item.removeAttribute('aria-current')); link.setAttribute('aria-current', 'location'); }
      else link.removeAttribute('aria-current');
    });
  }, { rootMargin: '-15% 0px -65% 0px' });
  links.forEach(link => { const section = document.querySelector(link.hash); if (section) observer.observe(section); });
}
