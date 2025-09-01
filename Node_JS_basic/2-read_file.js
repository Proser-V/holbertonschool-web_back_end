function countStudents(path) {
    const fs = require('fs');
    try {
        const data = fs.readFileSync(path, 'utf8');
        const lines = data.trim().split('\n');
        let counter = -1;
        lines.forEach(() => {
            counter += 1;
        })
        process.stdout.write(`Number of students: ${counter}\n`)
        const header = lines[0].split(',');
        const fieldIndex = header.indexOf('field');
        const firstNameIndex = header.indexOf('firstname');

        const fields = {};

        for (let i = 1; i < lines.length; i++) {
        const row = lines[i].split(",");
        const field = row[fieldIndex];
        const firstname = row[firstNameIndex];

        if (!fields[field]) {
            fields[field] = [];
        }
        fields[field].push(firstname);
        }
        for (const [field, names] of Object.entries(fields)) {
            process.stdout.write(`Number of students in ${field}: ${names.length}. List: ${names.join(", ")}\n`);
        }
    } catch (error) {
        throw new Error('Cannot load the database\n')
    }
}

module.exports = countStudents;