// ======================================================
// Surjagad Ispat — main.js
// Handles: Reveal, Counter, Navbar scroll, Mega-menu, Mobile drawer
// ======================================================

// ---- Reveal on scroll ----
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.classList.add('in');
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ---- Animated Counter ----
function animateCounter(el) {
  const to = parseFloat(el.dataset.to || 0);
  const decimals = parseInt(el.dataset.decimals || 0);
  const suffix = el.dataset.suffix || '';
  const prefix = el.dataset.prefix || '';
  const duration = 2200;
  const start = performance.now();

  function tick(now) {
    const t = Math.min(1, (now - start) / duration);
    const eased = 1 - Math.pow(1 - t, 3);
    const val = eased * to;
    el.textContent = prefix + val.toLocaleString('en-US', {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals
    }) + suffix;
    if (t < 1) requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
}

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting && !e.target.dataset.started) {
      e.target.dataset.started = '1';
      animateCounter(e.target);
    }
  });
}, { threshold: 0.4 });

document.querySelectorAll('.counter').forEach(el => counterObserver.observe(el));

// ---- Navbar scroll behaviour ----
const topBar = document.getElementById('top-bar');
const mainHeader = document.getElementById('main-header');
const navSpacer = document.getElementById('nav-spacer');

function onScroll() {
  const scrolled = window.scrollY > 24;
  if (topBar) {
    topBar.classList.toggle('hidden-bar', scrolled);
  }
  if (mainHeader) {
    mainHeader.classList.toggle('scrolled', scrolled);
  }
  if (navSpacer) {
    navSpacer.style.height = scrolled ? '5rem' : '7rem';
  }
}

window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// ---- Mega Menu ----
const desktopNav = document.querySelector('.desktop-nav');
let currentMega = null;

if (desktopNav) {
  desktopNav.querySelectorAll('.nav-item[data-mega]').forEach(item => {
    const megaId = item.dataset.mega;
    const megaEl = document.getElementById(megaId);
    if (!megaEl) return;

    item.addEventListener('mouseenter', () => {
      if (currentMega && currentMega !== megaEl) currentMega.classList.remove('open');
      megaEl.classList.add('open');
      currentMega = megaEl;
    });
  });

  mainHeader && mainHeader.addEventListener('mouseleave', () => {
    document.querySelectorAll('.mega-menu').forEach(m => m.classList.remove('open'));
    currentMega = null;
  });
}

// ---- Mobile Drawer ----
const mobileOverlay = document.getElementById('mobile-overlay');
const openBtn = document.getElementById('open-menu');
const closeBtn = document.getElementById('close-menu');
const mobileBg = document.getElementById('mobile-bg');

function openDrawer() { mobileOverlay && mobileOverlay.classList.add('open'); }
function closeDrawer() { mobileOverlay && mobileOverlay.classList.remove('open'); }

openBtn && openBtn.addEventListener('click', openDrawer);
closeBtn && closeBtn.addEventListener('click', closeDrawer);
mobileBg && mobileBg.addEventListener('click', closeDrawer);

// Close drawer on link click
mobileOverlay && mobileOverlay.querySelectorAll('a').forEach(a => a.addEventListener('click', closeDrawer));
