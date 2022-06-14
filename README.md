# libstp

stp_template_t
stp_template_id()
stp_template_domain()
stp_template_tag()
stp_template_stencil()
stp_template_validate()

stp_validate_domain()
stp_validate_tag()
stp_validate_stencil()


enum stp_rule_id {
    STP_RULE_ID_LOAD,
    STP_RULE_ID_LIST,
    STP_RULE_ID_CREATE,
    STP_RULE_ID_UPDATE,
    STP_RULE_ID_DELETE,
    STP_RULE_ID_PRINT
};

typedef int (cy_rule_validator_f)(const cy_json_t *data, cy_json_t **errors);
typedef cy_json_t *(cy_rule_executor_f)(const cy_json_t *data);
typedef void (cy_rule_ehandler_f)(const cy_json_t *data, const cy_json_t *errors);

struct cy_rule_t {
    int id;
    cy_rule_validator_f *validator;
    cy_rule_executor_f *executor;
    cy_rule_ehandler_f *ehandler;
    cy_json_t *data;
};


cy_rule_t *
cy_rule_new(int id, cy_rule_validator_f *validator, cy_rule_executor_f *executor, cy_rule_ehandler_f *eh, cy_json_t *data);

stp_rule_t *
stp_rule_copy(const stp_rule_t *);

stp_rule_t *
stp_rule_clone(const stp_rule_t *);

void
stp_rule_free(const stp_rule_t **);

bool
stp_rule_valid(const stp_rule_t *);

void *
stp_rule_exec(const stp_rule_t *);


stp_rule_t *r = stp_rule_factory(STP_RULE_ID_LOAD, data, NULL);

cy_rule_data_t;
cy_string_t *c_rule_data_get(size_t key);
void cy_rule_data_set(size_t key, cy_string_t *val);
bool cy_rule_data_exists(size_t key)
