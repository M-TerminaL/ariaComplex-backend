// start swiper slider top main Js

let swiper = new Swiper(".swiper-container", {
    slidesPerView: '1',
    spaceBetween: 30,
    centeredSlides: true,
    loop: true,
    autoplay: {
        delay: 3000
    },
    effect: "fade",
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    // pagination: {
    //   el: ".swiper-pagination",
    //   clickable: true,
    // },
});
// end swiper slider top main js


// Start Swiper Slider Services 

let swiper1 = new Swiper(".swiper-container1", {
    effect: "coverflow",

    grabCursor: true,
    centeredSlides: true,
    autoplay: {
        speed: 3000
    },
    breakpoints: {
        '0': {
            slidesPerView: 1,
        },
        // '768': {
        //   slidesPerView: 1,
        //   },
        // '992' : {
        //     slidesPerView: 2
        // }
    },

    slidesPerView: "auto",
    coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
    },
    // pagination: {
    //   el: ".swiper-pagination",
    // },
});


// Finish Swiper Slider Services
/* Start Close & Open Navbar Button In Mobile & Tablet */

const navCloseElem = document.getElementById('close')
const navMenuBtnElem = document.getElementById('menu-btn')
const navbarMenuElem = document.getElementById('navbar-mob')

function navbarClose() {
    navbarMenuElem.classList.remove('navbar-toggle')
}

function navbarOpen() {
    navbarMenuElem.classList.add('navbar-toggle')
}

navCloseElem.addEventListener('click', navbarClose)
navMenuBtnElem.addEventListener('click', navbarOpen)

/* End Close & Open Navbar Button In Mobile & Tablet */

/* Start Menu Button and Services Panel options in Responsive Navbar mobile  */

const ServicesItems = document.getElementById('category-items')
const menuButton = document.getElementById('menu')
const servicesButton = document.getElementById('category')
const menuItems = document.getElementById('menu-items')

function openServicesItems() {
    ServicesItems.style.display = 'block'
    menuItems.style.display = 'none'
    servicesButton.style.backgroundColor = 'var(--clr-primary)'
    menuButton.style.backgroundColor = '#f5f3f4'
    servicesButton.style.color = 'var(--clr-white)'
    menuButton.style.color = 'var(--clr-black)'
}

function openMenuItems() {
    menuItems.style.display = 'block'
    ServicesItems.style.display = 'none'
    menuButton.style.backgroundColor = 'var(--clr-primary)'
    servicesButton.style.backgroundColor = '#f5f3f4'
    menuButton.style.color = 'var(--clr-white)'
    servicesButton.style.color = 'var(--clr-black)'
}

servicesButton.addEventListener('click', openServicesItems)
menuButton.addEventListener('click', openMenuItems)

/* End Menu Button and Services Panel options in Responsive Navbar mobile  */


/* start services gallery slider */

let swiper2 = new Swiper(".swiper-container2", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    autoplay: {
        speed: 3000
    },
    coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: false,
    },
    // pagination: {
    //   el: ".swiper-pagination",
    // },
});

/* end services gallery slider */

/* Start Show Sub Menu with Js */
const subMenuElem = document.getElementById('sub-menu')
const servicesItem = document.getElementById('services')

const homeLiElem = document.getElementById('no-sub-home')
const priceLiElem = document.getElementById('no-sub-price')
const contactLiElem = document.getElementById('no-sub-contact')
const aboutLiElem = document.getElementById('no-sub-about')
const headerDocElem = document.getElementsByTagName('header')

function showSubMenuElem() {
    subMenuElem.style.display = 'block'
}

function hideSubMenuElem() {
    subMenuElem.style.display = 'none'
}

servicesItem.addEventListener('mouseenter', showSubMenuElem)
subMenuElem.addEventListener('mouseleave', hideSubMenuElem)
homeLiElem.addEventListener('mouseenter', hideSubMenuElem)
priceLiElem.addEventListener('mouseenter', hideSubMenuElem)
contactLiElem.addEventListener('mouseenter', hideSubMenuElem)
aboutLiElem.addEventListener('mouseenter', hideSubMenuElem)
headerDocElem[0].addEventListener('mouseenter', hideSubMenuElem)


/* End Show Sub Menu with Js */

/* Start Preloader */

const preloader = document.getElementById('preloader-container')

document.addEventListener('DOMContentLoaded', function () {
    preloader.style.display = 'none'
})

// window.onload = function () {
//   preloader.style.display = 'none'
// }

/* End Preloader */


/* start scroll top */

const scrollTop = document.getElementById('arrow-up')

function scrollTopDom() {
    globalThis.scrollTo({top: 0, left: 0, behavior: 'smooth'})
}


scrollTop.addEventListener('click', scrollTopDom)


/* end scroll top */

var lastKnownScrollY = 0;
var currentScrollY = 0;
var idOfHeader = 'header';
var eleHeader = null;
const classes = {
  pinned: 'header-pin',
  unpinned: 'header-unpin',
};
function onScroll() {
  currentScrollY = window.pageYOffset;
  if (currentScrollY < lastKnownScrollY) {
    pin();
  } else if (currentScrollY > lastKnownScrollY) {
    unpin();
  }
  lastKnownScrollY = currentScrollY;
}
function pin() {
  if (eleHeader.classList.contains(classes.unpinned)) {
    eleHeader.classList.remove(classes.unpinned);
    eleHeader.classList.add(classes.pinned);
  }
}
function unpin() {
  if (eleHeader.classList.contains(classes.pinned) || !eleHeader.classList.contains(classes.unpinned)) {
    eleHeader.classList.remove(classes.pinned);
    eleHeader.classList.add(classes.unpinned);
  }
}
window.onload = function() {
  eleHeader = document.getElementById(idOfHeader);
  document.addEventListener('scroll', onScroll, false);
}






