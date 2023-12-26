/* 
  let this be a warngin
  this is a cluster fuck, please do not modify unless nessarry
  please refrane from moving non-txt files
  the story.json and url format must be followed
  reader.html?story=[story_id]
  ensure story/*.txt exists if defined in story.json
  ensure story/*.txt format are followed
*/
const urlPrams = new URLSearchParams(window.location.search);
const story_id = urlPrams.get("story");
const lang = urlPrams.get("lang", "zh") || "zh";

function load_story(story_id, lang) {
  fetch("storys/story.json")
    .then(r => r.json())
    .then(r => {
      let url = "reader.html?";
      let lang_s = document.getElementById("lang_selector");
      let story = r[story_id][lang];
      let title = story["title"];
      
      document.getElementById("story_title").innerHTML = title;
      document.title = `Story Reader - ${title}`;
      
      if (lang === "en") {
        lang_s.setAttribute("href", `${url}lang=zh&story=${story_id}`);
        lang_s.innerHTML = "繁體中文";
        
      } else if (lang === "zh") {
        lang_s.setAttribute("href", `${url}lang=en&story=${story_id}`);
        lang_s.innerHTML = "English";
      }
      
      return fetch(story["content_url"]);
    })
    .then(r => r.text())
    .then(r => {
      let paragraph = r.split("\n");
      
      paragraph.forEach((i) => {
        let para = document.createElement("p");
        para.textContent = i;
        document.getElementById("story_content").appendChild(para);
      });
    })
    .catch((err) => {
      console.log("Error loading story:", err);
    });
}

load_story(story_id, lang);
