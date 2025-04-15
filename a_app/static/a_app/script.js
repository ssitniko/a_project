
const nameInput = document.getElementById('nameInput');
const emailInput = document.getElementById('emailInput');
const feedbackInput = document.getElementById('feedbackInput');
const ratingInput = document.querySelector('input[name="rating"]');
const addButton = document.getElementById('addButton');
const nameOutput = document.getElementById('nameOutput');

function updateList() {
  nameOutput.innerHTML = '';
  const items = JSON.parse(localStorage.getItem('items') || '[]');

  items.forEach(item => {
    if (item.name && item.feedback && item.rating) {
      const listItem = document.createElement('li');
      listItem.classList.add('mb-3');

      const nameElement = document.createElement('strong');
      nameElement.textContent = item.name;

      const ratingElement = document.createElement('span');
      ratingElement.textContent = ` ★ ${item.rating}`;

      const feedbackElement = document.createElement('p');
      feedbackElement.textContent = item.feedback;

      listItem.appendChild(nameElement);
      listItem.appendChild(ratingElement);
      listItem.appendChild(document.createElement('br'));
      listItem.appendChild(feedbackElement);

      nameOutput.appendChild(listItem);
    }
  });
}

addButton.addEventListener('click', () => {
  const nameValue = nameInput.value.trim();
  const emailValue = emailInput.value.trim();
  const feedbackValue = feedbackInput.value.trim();
  const ratingValue = ratingInput.value.trim();

  if (nameValue && emailValue && feedbackValue && ratingValue) {
    const items = JSON.parse(localStorage.getItem('items') || '[]');
    items.push({
      name: nameValue,
      email: emailValue,
      feedback: feedbackValue,
      rating: ratingValue
    });

    localStorage.setItem('items', JSON.stringify(items));

    nameInput.value = '';
    emailInput.value = '';
    feedbackInput.value = '';
    ratingInput.value = '';

    updateList();
  }
});

updateList();