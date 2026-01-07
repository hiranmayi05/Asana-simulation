-- ORGANIZATIONS
CREATE TABLE organizations (
  org_id TEXT PRIMARY KEY,
  name TEXT,
  domain TEXT,
  created_at TIMESTAMP
);

-- TEAMS
CREATE TABLE teams (
  team_id TEXT PRIMARY KEY,
  org_id TEXT,
  name TEXT,
  function TEXT
);

-- USERS
CREATE TABLE users (
  user_id TEXT PRIMARY KEY,
  org_id TEXT,
  name TEXT,
  email TEXT,
  role TEXT,
  created_at TIMESTAMP
);

-- TEAM MEMBERSHIPS
CREATE TABLE team_memberships (
  team_id TEXT,
  user_id TEXT,
  PRIMARY KEY (team_id, user_id)
);

-- PROJECTS
CREATE TABLE projects (
  project_id TEXT PRIMARY KEY,
  team_id TEXT,
  name TEXT,
  project_type TEXT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP
);

-- SECTIONS
CREATE TABLE sections (
  section_id TEXT PRIMARY KEY,
  project_id TEXT,
  name TEXT,
  position INTEGER
);

-- TASKS
CREATE TABLE tasks (
  task_id TEXT PRIMARY KEY,
  project_id TEXT,
  section_id TEXT,
  parent_task_id TEXT,
  name TEXT,
  description TEXT,
  assignee_id TEXT,
  due_date DATE,
  completed BOOLEAN,
  created_at TIMESTAMP,
  completed_at TIMESTAMP
);

-- COMMENTS
CREATE TABLE comments (
  comment_id TEXT PRIMARY KEY,
  task_id TEXT,
  user_id TEXT,
  content TEXT,
  created_at TIMESTAMP
);

-- CUSTOM FIELDS
CREATE TABLE custom_fields (
  field_id TEXT PRIMARY KEY,
  project_id TEXT,
  name TEXT,
  field_type TEXT
);

-- CUSTOM FIELD VALUES
CREATE TABLE custom_field_values (
  field_id TEXT,
  task_id TEXT,
  value TEXT,
  PRIMARY KEY (field_id, task_id)
);

-- TAGS
CREATE TABLE tags (
  tag_id TEXT PRIMARY KEY,
  name TEXT
);

-- TASK TAGS
CREATE TABLE task_tags (
  task_id TEXT,
  tag_id TEXT,
  PRIMARY KEY (task_id, tag_id)
);
