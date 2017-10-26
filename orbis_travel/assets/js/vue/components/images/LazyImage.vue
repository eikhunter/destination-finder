<template>
  <figure class="img-Image">
    <div class="img-Image_AspectRatioHolder">
      <div class="img-Image_AspectRatio"
           :style="{ 'paddingBottom': aspectRatio }"></div>

      <div class="img-Image_Media" ref="media">
        <img alt=""
             :src="imageUrl"
             :class="[
                 'img-Image_Image',
                 'img-Image_Image-small',
                 { 'img-Image_Image-blurred': blur }
               ]"
             ref="image">
      </div>
    </div>
  </figure>
</template>

<script>
  export default {
    props: {
      aspectRatio: {
        type: String,
        required: true
      },
      smallImageUrl: {
        type: String,
        required: true
      },
      largeImageUrl: {
        type: String,
        required: true
      },
      altText: {
        type: String,
        required: false,
        default: ''
      },
      blur: {
        type: Boolean,
        required: false,
        default: true
      }
    },

    data () {
      const imageUrl = this.blur ? this.smallImageUrl : this.largeImageUrl

      return {
        imageUrl,
        smallImage: undefined,
        largeImage: undefined
      }
    },

    created () {
      this.largeImage = new Image()
      this.largeImage.src = this.largeImageUrl
      this.largeImage.className = 'img-Image_Image img-Image_Image-large'
      this.largeImage.onload = () => {
        this.largeImage.classList.add('img-Image_Image-loaded')
      }

      if (this.altText) {
        this.largeImage.alt = this.altText
      }

      if (this.blur) {
        this.smallImage = new Image()
        this.smallImage.src = this.smallImageUrl

        this.largeImage.addEventListener('transitionend', () => {
          this.$refs.media.classList.add('img-Image_Media-largeLoaded')
        })
      }
    },

    mounted () {
      const media = this.$refs.media
      media.appendChild(this.largeImage)

      if (this.blur) {
        this.smallImage.onload = () => {
          this.$refs.image.classList.add('img-Image_Image-loaded')
        }
      }

      // This is used for IE since they don't support object-fit
      const largeDiv = document.createElement('div')
      largeDiv.className = 'img-Image_Image img-Image_Image-ie img-Image_Image-loaded'
      largeDiv.style.backgroundImage = `url('${this.largeImageUrl}')`
      media.appendChild(largeDiv)
    }
  }
</script>
