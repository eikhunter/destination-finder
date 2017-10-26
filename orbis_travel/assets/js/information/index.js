import Siema from 'siema'

export class InformationCarousel {
  constructor ({ el }) {
    const { className } = el
    const _this = this

    this.els = {
      el,
      items: el.querySelector(`.${className}_Items`),
      controls: {
        el: el.querySelector(`.${className}_Controls`),
        prev: el.querySelector(`.${className}_Control-prev`),
        next: el.querySelector(`.${className}_Control-next`)
      }
    }
    this.carouselConfig = {
      selector: this.els.items,
      easing: 'cubic-bezier(0.86, 0, 0.07, 1)',
      perPage: 1,
      onInit () {
        _this.els.controls.next.setAttribute('touch-action', 'none')
        _this.els.controls.prev.setAttribute('touch-action', 'none')
        _this.els.controls.next.addEventListener('pointerdown', () => {
          this.next()
        })
        _this.els.controls.prev.addEventListener('pointerdown', () => {
          this.prev()
        })
      }
    }
    this.carousel = this.initCarousel()
  }

  initCarousel () {
    return new Siema(this.carouselConfig)
  }
}
